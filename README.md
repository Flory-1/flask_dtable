![flask_dtable](flask_dtable.png)
# flask_dtable a Full-Featured Table System made with Python by Florian L&auml;mmlein
#### Create an HTML Table and return it as an string.
&nbsp;
&nbsp;
***
## flask_dtable Features
- HTML forms
- Column Editor
- Column replace
- Includes Datatables
- Custom column filters
- Live feedback handler
- Custom column popups
&nbsp;
&nbsp;
***
## How to Install
pip install flask_dtable
&nbsp;
&nbsp;
***
## flask_dtable Parameters
| <strong >Param</strong> | <strong >Description</strong> | <strong >Dict Params</strong> | <strong >Dict Description</strong> | <strong >Type</strong> | <strong >Default Value</strong> |
| --- | --- | --- | --- | --- | --- |
| data | Table content as an list of str | | | list | `[[]]` |
| &nbsp; | | | | | |
| section | Datareplacements by an position index | active | Status of the current function | bool | `False` |
| | | position | Replacement position as int (by data index) | ​list, (int, str (`'_sec'`)) | `[]` |
| | | value | Replacement value as (str or current data value) | list, (list, str (`'_var'`)) | `[[]]` |
| | | check | Data replacement check as function (by data index) | list | `[[]]` |
| &nbsp; | | | | | |
| header | Table Header names as an list of str | value | Table header Names as str | list | `[]` |
| | | class | Table header class | str | `None` |
| | | id | Table header id | str | `None` |
| &nbsp; | | | | | |
| footer | Table Footer names as an list of str | active | Status of the current function | bool | `False` |
| | | value | Table footer Names as str | list | `[]` |
| | | class | Table footer class | str | `None` |
| | | id | Table footer id | str | `None` |
| | | calculate | Table calculate function by index from column | list, int | `[]` |
| | | decimal_places | Table calculate precision numbers | int | `2` |
| &nbsp; | | | | | |
| form | Data Column Editor | active | Status of the current function | bool | `False` |
| | | position | Form position as int (by data index) | ​list, (int, str (`'_sec'`)) | `[]` |
| | | action | From action | ​str, list (`'_tab'`, int) | `None` |
| | | class | From class | str | `None` |
| | | tooltip_text | From submit button tooltip text as str | ​list, str | `[]` |
| | | button_color | From submit button color as str | ​list, str | `[]` |
| | | icon | From submit button icon as str | ​list, str | `[]` |
| | | [request_out](#Special-Parameters) | Form fields outside the form as list, str | `dict` | `{}` |
| | | [request_in](#Special-Parameters) | Form fields inside the form as list, str | ​`dict` | `{}` |
| &nbsp; | | | | | |
| script | Datatables script tag | active | Status of the current function | bool | `False` |
| | | responsive | Status of the responsive function | ​​bool | `False` |
| | | fixed | Set fixed columns (by data index) | int | `None` |
| | | order | Column orders ([`1`, `'asc'`], [`1`, `'desc'`]) | ​list, (int, str (`'asc'`, `'desc'`)) | `[]` |
| | | length_menu | Enable/Disable the length menu | bool | `True` |
| | | [buttons](#Special-Parameters) | Table buttons as dicts | `list` | `[]` |
| | | [child_rows](#Special-Parameters) | Child rows as dicts | `list` | `[]` |
| | | [live_feed](#Special-Parameters) | Live feedback as dicts | `dict` | `{}` |
| &nbsp; | | | | | |
| editor | Tableeditor script tag | active | Status of the current function | bool | `False` |
| | | action | HTML form action | str | `None` |
| | | label | Editor Modal display Name | str | `None` |
| | | size | Editor Modal display size (`'small'`, `'large'`) | str | `small` |
| | | [fields](#Special-Parameters) | Editor fields as dicts | `list` | `[]` |
| | | [order](#Special-Parameters) | Editor div order as lists | `list` | `[]` |
| | | [chars](#Special-Parameters) | Editor field value chars replace as functions | `dict` | `{}` |
| &nbsp; | | | | | |
| popup | New window popup on `tr` click | active | Status of the current function | bool | `False` |
| | | url | Window main url | str | `None` |
| | | width | Popup window width | int | `1600` |
| | | height | Popup window height | int | `1000` |
| | | params | Window url parameters set name as str and value (by data index) | list, list (str, int) | `[[]]` |
&nbsp;
&nbsp;
***
## flask_dtable Special Parameters
| <strong >Main Param</strong> | <strong >Param</strong> | <strong >Dict Param</strong> | <strong >Description</strong> | <strong >Type</strong> | <strong >Default Value</strong> |
| --- | --- | --- | --- | --- | --- |
| ​form | request_out | request_name | Datafield name | list, str | `[]` |
| | | request_id | Datafield id | ​list, str | `[]` |
| | | rquest_value | Datafield value (by data index or (`'_sec'`)) | ​list, str | `[]` |
| | | value | Datafield replacement value if `'_sec'` is set | ​list, list, str | `[[]]` |
| | | check | Datafield replacement check as function (by data index) | ​list, list, str | `[[]]` |
| | request_out | request_name | Datafield name | list, str | `[]` |
| | | request_id | Datafield id | ​list, str | `[]` |
| | | rquest_value | Datafield value (by data index or (`'_sec'`)) | ​list, str | `[]` |
| | | value | Datafield replacement value if `'_sec'` is set | ​list, list, str | `[[]]` |
| | | check | Datafield replacement check as function (by data index) | ​list, list, str | `[[]]` |
| &nbsp; | | | | | |
| script | buttons | button_name | Holds the display name from the buttons |  str | `Actions` |
| | | export | Export buttons (`'pdf'`, `'excel'`, `'csv'`) | ​list, str | `[]` |
| | | hidde | Set the hidde button | ​bool | `False` |
| | | nohidde | Don´t hidde this columns (by column index) | list, int | `[]` |
| | | filter | Set the filter button (by column index) | list, int | `[]` |
| | | [custom_filter](#Special-Parameters) | Set custom filters as dicts | list, dict | `[]` |
| | | [data_filter](#Special-Parameters) | Set data filters (creates url get parameters) as dicts | list, dict | `[]` |
| | custom_filter | name | Display name from filter | str | `None` |
| | | labels | Display values from filter row | list, str | `[]` |
| | | values | Check the values (by the data section as str) | list, str | `[]` |
| | data_filter | name | Display name from filter | str | `None` |
| | | labels | Display values from filter row | list, str | `[]` |
| | | values | Check the values (by the data section as str) | list, str | `[]` |
| | child_rows | label | Display name from child row | str | `None` |
| | | column | Display value from child row (by data index) | int | `None` |
| | live_feed | label | Display name from live feedback | str | `None` |
| | | column | Fallback value from child row (by data index) | int | `0` |
| | | [update](#Special-Parameters) | Set data filters (creates ajax post parameters) | dict | `{}` |
| | | [handler](#Special-Parameters) | Set data filters live handler (creates ajax post) as dicts | dict | `{}` |
| | update | url | Ajax url to an blueprint | str | `None` |
| | | value | Ajax post values (by data index) | str | `None` |
| | handler | type | Ajax update input type | str | `None` |
| | | post | Ajax update post id, name | str | `None` |
| | | column | Ajax update column (by data index) | str | `None` |
| &nbsp; | | | | | |
| editor | fields | label | Display form field name | str | `None` |
| | | column | Display form field value (by column index) | int | `0` |
| | | check | Field value to check only if type is radio | int | `1` |
| | | class | Display form field class | ​str | `None` |
| | | name | Display form field name | str | `None` |
| | | id | Display form field id | str | `None` |
| | | type | Display form field type | str | `None` |
| | | required | Field required check | ​bool | `False` |
| | | disabled | Field disabled check | ​bool | `False` |
| | | hidden | Field hidden check | ​bool | `False` |
| | order | index | div order index (How many fields in one div are shown) | int | `2` |
| | | index_lower | div order index (if index is to short index_lower is active) | int | `2` |
| | | class | div order classes | str | `col-md-12 col-lg-6` |
| | | class_lower | div order classes (if index_lower is active class_lower is set) | str | `col-md-12 col-lg-12` |
| | chars | | Field replace tags (special characters) as functions | | `{`<br>&nbsp;`ord('ä'):'ae',`<br>&nbsp;`ord('ü'):'ue',`<br>&nbsp;`ord('ö'):'oe'`<br>`}` |
&nbsp;
&nbsp;
***
## flask_dtable Examples
<strong >Basic usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    }
)
```
<strong >Datatables usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    script = {
        "active": True
    }
)
```
<strong >Datareplacement usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    section = {
        "active": True,
        "position": [0, "_sec"],
        "value": [
            ['Kein Geburtstag', ['_var', 1]]
        ],
        "check": [
            ['data[1] == "02.11.2001"']
        ]
    },
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    script = {
        "active": True
    }
)
```
<strong >Data editor usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    script = {
        "active": True
    },
    editor = {
        "active": True,
        "fields": [
            {
                "label": "Name", 
                "column": 0, 
                "disabled": True
            },
            {
                "label": "Geburtstag", 
                "column": 1, 
                "required": True
            }
        ]
    }
)
```
<strong >Child rows usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    script = {
        "active": True,
        "child_rows": [
            {
                "label": "Zusatz",
                "column": 2
            }
        ]
    }
)
```
<strong >Datatable order usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Zusatz"
        ]
    },
    script = {
        "active": True,
        "order": [
            [0, 'asc'],
            [1, 'asc']
        ]
    }
)
```
<strong >Datatable button usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Zusatz"
        ]
    },
    script = {
        "active": True,
        "buttons": {
            "export": ['pdf', 'excel']
        }
    }
)
```
<strong >Datatable filter button usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Zusatz"
        ]
    },
    script = {
        "active": True,
        "buttons": {
            "filter": [0,2]
        }
    }
)
```
<strong >Datatable filter button with custom filter usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Zusatz"
        ]
    },
    script = {
        "active": True,
        "buttons": {
            "custom_filter": [
                {
                    "name": "Geburtstag",
                    "labels": ["November"],
                    "values": ["data[1].split('.')[1] == '11'"]
                }
            ]
        }
    }
)
```
<strong >Datatable filter button with data filter usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000', 'Hallo Welt 1'],
        ['Peter', '02.11.2001', 'Hallo Welt 2']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Zusatz"
        ]
    },
    script = {
        "active": True,
        "buttons": {
            "data_filter": [
                {
                    "name": "Geburtstag",
                    "labels": ["November", "Dezember"],
                    "values": ["11", "12"]
                }
            ]
        }
    }
)
```
<strong >Form basic usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Action:"
        ]
    },
    form = {
        "active": True,
        "action": "/submit_page",
        "position": 2,
        "request_in": {
            "request_name": "name",
            "request_value": 0
        }
    },
    script = {
        "active": True
    }
)
```
<strong >Form data replacement usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag",
            "Action:"
        ]
    },
    form = {
        "active": True,
        "action": "/submit_page",
        "position": 2,
        "request_in": {
            "request_name": ["name", "birthday"],
            "request_value": [0, "_sec"]
        },
        "value": [
            ["Kein Geburtstag", ["_var", 1]]
        ],
        "check": [
            ["data[1] == '02.11.2001'"]
        ]
    },
    script = {
        "active": True
    }
)
```
<strong >Live feedback usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    script = {
        "active": True,
        "live_feed": {
            "label": "Mein Geburtstag",
            "column": 1,
            "update": {
                "url": "preview",
                "value": [
                    {"post": "birthday", "column": 1}
                ]
            }
        }
    }
)
```
<strong >Popup usage:</strong>
```python
flask_dtable(
    data = [
        ['Niklas', '13.09.2000'],
        ['Peter', '02.11.2001']
    ],
    header = {
        "value": [
            "Name",
            "Geburtstag"
        ]
    },
    popup = {
        "active": True,
        "url": "/edit",
        "params": [
            ["birthday", 1]
        ]
    }
)
```
&nbsp;
&nbsp;
***
## Legacy versions
This version of the flask_dtable are the acctual stable version which is compatible with Python 3+ and is supported for feature updates.

## Do you have any Ideas, Changes or Bugs ?
Please let me know in the Comments, i will try to fix or add waht you found/want :D