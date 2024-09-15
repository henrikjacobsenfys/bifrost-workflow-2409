import typer
from loguru import logger
from tqdm import tqdm
import pooch

from bifrost2409.config import RAW_DATA_DIR, META_DATA_DIR
from bifrost2409 import __version__

app = typer.Typer()

MR_MANAGER = pooch.create(
    path=RAW_DATA_DIR,
    base_url="https://project.esss.dk/nextcloud/index.php/s/Diq9n3kITaEBtq7/",
    version=__version__ if '+' in __version__ else __version__ + '+alpha', # force Pooch to use the "main" folder to avoid re-downloading large files
    version_dev="main",
    registry=None,
)
MR_MANAGER.load_registry(META_DATA_DIR / "pooch-registry.txt")

FILELIST = (
    "20240829/BIFROST_20240829T192305.h5",  # elastic incoherent
    "20240902/BIFROST_20240902T163047.h5",  # elastic + inelastic incoherent
    "20240914/BIFROST_20240914T053723.h5",  # elastic incoherent + phonon
)

@app.command()
def download_datafiles(files: list[str] = FILELIST):
    for file in tqdm(files, desc="Fetching"):
        MR_MANAGER.fetch(file, progressbar=True)


if __name__ == "__main__":
    app()
