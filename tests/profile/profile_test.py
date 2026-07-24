import cProfile
import pstats
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def run_profile():
    for _ in range(100):
        client.get("/users")
        client.get("/tickets")


if __name__ == "__main__":
    profiler = cProfile.Profile()

    profiler.enable()

    run_profile()

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(20)

    #save profile test result
    stats.dump_stats("tests/profile/profile_results.prof")
