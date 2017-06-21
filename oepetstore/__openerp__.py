{
    'name' : 'OpenERP Pet Store',
    'version': '1.0',
    'author': "Vittoria Conseil",
    'summary': 'Sell pet toys',
    'category': 'Tools',
    'description':
        """
OpenERP Pet Store
=================

A wonderful application to sell pet toys.
        """,
    'data': [
        "petstore.xml",
        "petstore_data.xml",
        "oepetstore.message_of_the_day.csv",
    ],
    'depends' : ['web', 'sale_stock'],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}
