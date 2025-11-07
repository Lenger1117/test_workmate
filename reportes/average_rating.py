from typing import List, Dict, Tuple
from collections import defaultdict


def generate_average_rating_report(data: List[Dict[str,str]]) -> List[Tuple[str, float]]:
    brand_ratings = defaultdict(list)
    for i in data:
        brand = i['brand'].strip().lower()
        try:
            rating = float(i['rating'])
        except ValueError:
            continue
        brand_ratings[brand].append(rating)

    result = []
    for brand, ratings in brand_ratings.items():
        avg_r = sum(ratings) / len(ratings)
        result.append(brand, avg_r)

    result.sort(key=lambda x: (-x[1], x[0]))
    return result