import ruamel.yaml
import os
from pathlib import Path

from mage_ai.settings.repo import get_repo_path

@custom
def load_profile(*args, **kwargs):
    local_dbt = get_repo_path() + '/dbt/jaffle_shop'
    local_dbt_path = Path(local_dbt)
    
    print('Writing demo profile...')
    
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True

    yml = yaml.load(f"""
    jaffle_shop:
        outputs:
            dev:
                type: postgres
                host: "{{{{ env_var('PG_HOST', 'host.docker.internal') }}}}"
                user: "{{{{ env_var('POSTGRES_USER', 'postgres') }}}}"
                password: "{{{{ env_var('POSTGRES_PASSWORD', 'postgres') }}}}"
                port: 5432
                dbname: "{{{{ env_var('POSTGRES_DB', 'public') }}}}"
                schema: "{{{{ env_var('POSTGRES_SCHEMA', 'analytics') }}}}"
                threads: 4
        target: dev
    """
    )

    with open(local_dbt + '/profiles.yml', 'w') as file:
        yaml.dump(yml, file)