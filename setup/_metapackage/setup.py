import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-import-export",
    description="Meta package for akretion-import-export Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-product_multi_category_import_export',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
