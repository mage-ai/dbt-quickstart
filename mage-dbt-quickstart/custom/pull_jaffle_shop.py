if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import git
from pathlib import Path
import shutil
import os

from mage_ai.settings.repo import get_repo_path

@custom
def pull_jaffle_shop(*args, **kwargs):

    repo_clone_url = "https://github.com/dbt-labs/jaffle_shop/"
    local_dbt = get_repo_path() + '/dbt/jaffle_shop'
    local_dbt_path = Path(local_dbt)

    if local_dbt_path.exists() and local_dbt_path.is_dir():
        print('Clearing existing models...')
        shutil.rmtree(local_dbt_path)
    
    print('Pulling repo...')
    repo = git.Repo.clone_from(repo_clone_url, local_dbt)