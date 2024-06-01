from pathlib import Path

data_dir = Path("data")
TABLE_NAME = "scores"
CON_KEY = "con"
PLAYER_COL_KEY = "player_col"

def get_db_file(constr):
    return constr.replace("sqlite:///", "")