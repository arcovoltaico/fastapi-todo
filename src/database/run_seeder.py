import argparse
import sys
from loguru import logger

sys.path = ['', '..'] + sys.path[1:]

from src.database.seeder import DevUser


seeder_mapping = {
    "devuser": DevUser,
}

argp = argparse.ArgumentParser(description='List the content of a folder')

argp.add_argument('seeders',
                    nargs="*",
                    help=(
                        'Names of the seeders you\'d like to run. The following seeders are available: '
                        f'{", ".join([k for k in seeder_mapping.keys()])}'
                        )
                    )

runnable_seeders = argp.parse_args().seeders

logger.info(f"Seeding for {len(runnable_seeders)} classes")

for s in runnable_seeders:
    if s not in seeder_mapping:
        raise KeyError((
            f"\"{s}\" is not a valid seeder. The following seeders are available: "
            f'{", ".join([k for k in seeder_mapping.keys()])}'
        ))

    seeder = seeder_mapping[s]()
    seeder.run()

logger.info(f"Seeding complete")