=====================
Product logistics UoM
=====================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:ee11361908c0caac2daf60ba1606ab59eb9a62844c53998cc70db390e2c56de5
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fproduct--attribute-lightgray.png?logo=github
    :target: https://github.com/OCA/product-attribute/tree/18.0/product_logistics_uom
    :alt: OCA/product-attribute
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/product-attribute-18-0/product-attribute-18-0-product_logistics_uom
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/product-attribute&target_branch=18.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module allows to choose an Unit Of Measure (UoM) for products
weight and volume. It can be set product per product for users in
group_uom.

Without this module, you only have the choice between Kg or Lb(s) and m³
for all the products.

For some business cases, you need to express in more precise UoM than
default ones like Liters instead of M³.

Even if you choose another UoM for the weight or volume, the system will
still store the value for these fields in the Odoo default UoM (Kg or
Lb(s) and m³). This ensures that the arithmetic operations on these
fields are correct and consistent with the rest of the addons.

Once this addon is installed values stored into the initial Volume and
Weight fields on the product and product template models are no more
rounded to the decimal precision defined for these fields. This could
lead to some side effects into reportss where these fields are used. You
can replace the fields by the new ones provided by this addon to avoid
this problem (product_volume and product_weight). In any cases, since
you use different UoM by product, you should most probably modify your
reportss to display the right UoM.

**Table of contents**

.. contents::
   :local:

Installation
============

Be aware, that this module only change the UoM but not the value.

It's the same behavior as base Odoo when you change from Metric System
to Imperial System.

Configuration
=============

To change the default UoM

1. Go "General Settings", then in "Products"
2. you have to select a default unit of measure for weights and volumes.

To change on a specific product

1. Go the product form you can change the UoM directly.

Usage
=====

Once installed and the 'Sell and purchase products in different units of
measure' option is enabled, the 'Unit of Measure' field will become
updatable on the 'Product' form for users with the permission 'Manage
Multiple Units of Measure'.

If the displayed value is 0.00 and a warning icon is displayed in front
of the unit of measure, it means that the value is too small to be
displayed in the current unit of measure. You should change the unit of
measure to a larger one to see the value.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/product-attribute/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/product-attribute/issues/new?body=module:%20product_logistics_uom%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Akretion
* ACSONE SA/NV

Contributors
------------

- Raphaël Reverdy <raphael.reverdy@akretion.com>
- Fernando La Chica <fernandolachica@gmail.com>
- Laurent Mignon <laurent.mignon@acsone.eu>
- Nhan Tran <nhant@trobz.com>

Other credits
-------------

The development of this module has been financially supported by:

- Akretion <https://akretion.com>
- La Base <https://labase.coop>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-hparfr| image:: https://github.com/hparfr.png?size=40px
    :target: https://github.com/hparfr
    :alt: hparfr

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-hparfr| 

This module is part of the `OCA/product-attribute <https://github.com/OCA/product-attribute/tree/18.0/product_logistics_uom>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
