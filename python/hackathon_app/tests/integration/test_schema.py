import schema
import sheets


def test_parse_schema(test_schema):
    """SchemaSheet should parse all schema."""
    actual = schema.SchemaSheet(lines=test_schema)
    assert isinstance(actual, schema.SchemaSheet)
    assert len(actual.tabs) > 0
    lines = actual.to_lines()
    assert test_schema == lines


def test_to_lines():
    line = "tab:col1,col2~old2"
    tab = schema.SchemaTab(line=line)
    lines = tab.to_lines()
    assert line == lines


def test_schema_compare(test_schema):
    """SchemaSheet should compare all schema."""
    model = sheets.get_model_schema()
    actual = schema.SchemaSheet(lines=test_schema)
    assert isinstance(model, schema.SchemaSheet)
    assert isinstance(actual, schema.SchemaSheet)
    assert len(actual.tabs) > 0


def test_schema_reader(create_test_sheet, cred_file):
    """SchemaSheet should read parse all schema."""
    spreadsheet_id = create_test_sheet["spreadsheetId"]
    reader = schema.SchemaReader(spreadsheet_id=spreadsheet_id, cred_file=cred_file)
    model = sheets.get_model_schema()
    delta = model.compare(reader.schema)
    assert len(delta) == 0
