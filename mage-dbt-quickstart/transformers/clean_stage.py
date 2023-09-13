if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # count letters in first name
    data['letters_first_name'] = data.apply(
        lambda row: len(row.first_name), axis=1
        )
    # is the name alliterative?
    data['is_alliterative'] = data.apply(
        lambda row: row.first_name[0].lower() == row.last_name[0].lower(), axis=1
        )

    return data


@test
def customer_id_is_unique(output, *args) -> None:
    """
    Check uniqueness of customer_id
    """
    assert len(set(output['customer_id'])) == len(output['customer_id']), 'Customer IDs are not unique'
