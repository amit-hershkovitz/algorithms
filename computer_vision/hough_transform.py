from typing import Tuple

import numpy as np


def lines_accumulator(edges: np.ndarray,
                      distances_resolution: float = 1,
                      angles_range: Tuple[float, float] = (0.0, np.pi),
                      angles_resolution: float = 0.5) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:

    edges_diagonal_len = np.sqrt(edges.shape[0] ** 2 + edges.shape[1] ** 2)
    distances = np.arange(-edges_diagonal_len, edges_diagonal_len, distances_resolution)
    angles = np.arange(angles_range[0], angles_range[1], angles_resolution)

    accumulator = np.zeros(shape=(len(angles), len(distances)))

    points = np.argwhere(edges == 1)

    for p, point in enumerate(points):
        for t, theta in enumerate(angles):
            distance = point[0] * np.cos(t) - point[1] * np.sin(t)
            d = np.argwhere(distances <= distance & distance < distances)
            accumulator[d, t] += 1

    return accumulator, angles, distances
