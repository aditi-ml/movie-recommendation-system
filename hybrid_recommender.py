import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# All genres
ALL_GENRES = [
    "Action", "Adventure", "Animation", "Children", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
    "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
    "Thriller", "War", "Western"
]

# Mood to genre mapping
_MOOD_MAP = {
    "Happy":      ["Comedy", "Animation", "Musical", "Children"],
    "Sad":        ["Drama", "Romance"],
    "Excited":    ["Action", "Adventure", "Thriller"],
    "Scared":     ["Horror", "Mystery", "Thriller"],
    "Romantic":   ["Romance", "Drama"],
    "Thoughtful": ["Documentary", "Drama", "Film-Noir"],
    "Adventurous":["Adventure", "Fantasy", "Sci-Fi", "Western"],
    "Relaxed":    ["Comedy", "Animation", "Musical"],
}

# Prepare genre matrix
movies["genre_list"] = movies["genres"].apply(
    lambda x: x.split("|") if x != "(no genres listed)" else []
)

mlb = MultiLabelBinarizer(classes=ALL_GENRES)
genre_matrix = pd.DataFrame(
    mlb.fit_transform(movies["genre_list"]),
    columns=mlb.classes_,
    index=movies.index
)

# Average ratings per movie
avg_ratings = (
    ratings.groupby("movieId")["rating"]
    .agg(["mean", "count"])
    .reset_index()
    .rename(columns={"mean": "avg_rating", "count": "num_ratings"})
)

movies_merged = movies.merge(avg_ratings, on="movieId", how="left")
movies_merged["avg_rating"] = movies_merged["avg_rating"].fillna(0)
movies_merged["num_ratings"] = movies_merged["num_ratings"].fillna(0)


def recommend_by_mood_and_genres(mood: str, selected_genres: list, k: int = 12):
    # Get mood genres
    mood_genres = _MOOD_MAP.get(mood, [])
    combined_genres = list(set(mood_genres + selected_genres))

    if not combined_genres:
        # No filter — return top rated
        top = movies_merged.nlargest(k, "avg_rating")
        top["score"] = top["avg_rating"] / 5.0
        return top[["movieId", "title", "genres", "score"]].reset_index(drop=True)

    # Build query vector
    query = pd.Series(0, index=ALL_GENRES)
    for g in combined_genres:
        if g in query.index:
            query[g] = 1

    # Cosine similarity
    sims = cosine_similarity([query.values], genre_matrix.values)[0]
    movies_merged["genre_score"] = sims

    # Normalize ratings
    max_ratings = movies_merged["num_ratings"].max()
    movies_merged["popularity_score"] = movies_merged["num_ratings"] / max_ratings

    # Combined score
    movies_merged["score"] = (
        0.5 * movies_merged["genre_score"] +
        0.3 * (movies_merged["avg_rating"] / 5.0) +
        0.2 * movies_merged["popularity_score"]
    )

    # Filter movies that have at least one matching genre
    mask = movies_merged["genre_score"] > 0
    result = movies_merged[mask].nlargest(k, "score")

    return result[["movieId", "title", "genres", "score"]].reset_index(drop=True)