from fastapi import APIRouter
from random import randint
from words import adjs, nouns, verbs

router = APIRouter()


@router.get("/")
async def index():
    # format: (num_wizards, verb, noun, adj)
    seed = (randint(1, 3), randint(0, 49), randint(0, 49), randint(0, 99))
    seed_serial = f"{seed[0]}.{seed[1]}.{seed[2]}.{seed[3]}"

    sentence = f"{seed[0]} wizards {verbs[seed[1]]} a {nouns[seed[2]]} {adjs[seed[3]]}."

    return {
            "seed": seed_serial,
            "prompt": sentence
        }
