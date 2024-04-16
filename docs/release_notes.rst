Release Notes
=============

.. towncrier release notes start

eth-typing v4.2.1 (2024-04-16)
------------------------------

Bugfixes
~~~~~~~~

- Put back types used for `EthPM`: `ContractName`, `Manifest`, and `URI`. (`#64 <https://github.com/ethereum/eth-typing/issues/64>`__)


eth-typing v4.2.0 (2024-04-15)
------------------------------

Features
~~~~~~~~

- Add type definitions to represent contract ``ABI``s. (`#61 <https://github.com/ethereum/eth-typing/issues/61>`__)


Removals
~~~~~~~~

- Remove types related to the EthPM module which has been removed from ``web3.py`` (`#60 <https://github.com/ethereum/eth-typing/issues/60>`__)


eth-typing v4.1.0 (2024-04-01)
------------------------------

Features
~~~~~~~~

- Add python3.12 support (`#57 <https://github.com/ethereum/eth-typing/issues/57>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge template updates, adding build tests for all docs formats, add ``blocklint`` to lint tools (`#57 <https://github.com/ethereum/eth-typing/issues/57>`__)


eth-typing v4.0.0 (2024-01-09)
------------------------------

Breaking changes
~~~~~~~~~~~~~~~~

- Drop python 3.7 support (`#55 <https://github.com/ethereum/eth-typing/issues/55>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge updates from the project template, notably: use ``pre-commit`` for linting and change the name of the ``master`` branch to ``main`` (`#55 <https://github.com/ethereum/eth-typing/issues/55>`__)
- Fixed booleans in ``pyproject.toml`` and added a test for the presence of the ``eth_typing.__version__`` attribute (`#56 <https://github.com/ethereum/eth-typing/issues/56>`__)


eth-typing v3.5.2 (2023-11-07)
------------------------------

Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- `#54 <https://github.com/ethereum/eth-typing/issues/54>`__


eth-typing v3.5.1 (2023-10-20)
------------------------------

Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add script to maintain Network constants listed in the networks module. (`#51 <https://github.com/ethereum/eth-typing/issues/51>`__)
- Add ``types-setuptools`` to support pkg_resources and __version__ (`#52 <https://github.com/ethereum/eth-typing/issues/52>`__)


eth-typing v3.5.0 (2023-09-29)
------------------------------

Features
~~~~~~~~

- Borrowing from the typing in web3.py, open up ``BlockIdentifier`` to include ``BlockParams`` (e.g. "latest", "finalized", etc..) as well as other valid values. (`#47 <https://github.com/ethereum/eth-typing/issues/47>`__)
- Add an ``IntEnum`` class, ``ChainId``, defining EVM-compatible network name enums as their respective chain id ``int`` values. (`#49 <https://github.com/ethereum/eth-typing/issues/49>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add the tests/ directory to the distributed tarball (`#46 <https://github.com/ethereum/eth-typing/issues/46>`__)
- Added ``build.os`` config for readthedocs (`#48 <https://github.com/ethereum/eth-typing/issues/48>`__)
- Fix release command by checking the git remote upstream configuration and merge other minor template updates. (`#50 <https://github.com/ethereum/eth-typing/issues/50>`__)


eth-typing v3.4.0 (2023-06-07)
------------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- pull in ethereum-python-project-template updates (`#44 <https://github.com/ethereum/eth-typing/issues/44>`__)


Features
~~~~~~~~

- Add ``Cancun`` to ``ForkName`` enum. (`#45 <https://github.com/ethereum/eth-typing/issues/45>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- remove unused docs deps, bump version of remaining (`#43 <https://github.com/ethereum/eth-typing/issues/43>`__)
- pull in ethereum-python-project-template updates (`#44 <https://github.com/ethereum/eth-typing/issues/44>`__)
- For CircleCI builds, update ``pip`` and pip install ``tox`` under sys instead of ``--user`` to avoid ``virtualenv`` versioning issues. (`#45 <https://github.com/ethereum/eth-typing/issues/45>`__)


v3.3.0 (2023-03-08)
-------------------

Features
~~~~~~~~

- Add ``Shanghai`` to ``ForkName`` enum. (`#39 <https://github.com/ethereum/eth-typing/issues/39>`__)
- Add support for python ``3.11``. (`#40 <https://github.com/ethereum/eth-typing/issues/40>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``tox`` related updates for ``make docs`` to work properly. Remove some old references to python ``3.5`` and ``3.6``. (`#39 <https://github.com/ethereum/eth-typing/issues/39>`__)
- Bump ``mypy`` version to ``0.910`` to avoid issues installing the "[dev]" extra on Python 3.10. Update test suite to require installing the full dependency suite to help catch these errors. (`#41 <https://github.com/ethereum/eth-typing/issues/41>`__)


v3.2.0 (2022-09-14)
-------------------

Features
~~~~~~~~

- Add ``Merge`` to ``ForkName`` enum (`#34 <https://github.com/ethereum/eth-typing/issues/34>`__)


Bugfixes
~~~~~~~~

- Pin Python version to <4 instead of <3.11 (`#37 <https://github.com/ethereum/eth-typing/issues/37>`__)
- Rename ``Merge`` to ``Paris`` in ``ForkNameEnum`` (`#38 <https://github.com/ethereum/eth-typing/issues/38>`__)


v3.1.0 (2022-06-22)
-------------------

Features
~~~~~~~~

- Setup towncrier to generate release notes from fragment files to ensure a higher standard
  for release notes. (`#16 <https://github.com/ethereum/eth-typing/issues/16>`__)
- Add new ``BLSPrivateKey`` type for BLS private key (`#23 <https://github.com/ethereum/eth-typing/issues/23>`__)
- Add ``__all__`` property to ``__init__.py`` with appropriate types to explicitly export (`#28 <https://github.com/ethereum/eth-typing/issues/28>`__)
- Add ``GrayGlacier`` to ``ForkName`` enum (`#30 <https://github.com/ethereum/eth-typing/issues/30>`__)


Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- `#32 <https://github.com/ethereum/eth-typing/issues/32>`__


v3.0.0 (2021-11-15)
-------------------

- Update ``ForkName`` enum to include ``Berlin``, ``London``, and ``ArrowGlacier``
- Update Python support to include python 3.8-3.10
- Remove Python 3.5 support

v2.2.0 (2019-10-31)
-------------------

- Update ``ForkName`` enum to include ``ConstantinopleFix`` and ``Istanbul``

v2.1.0 (2019-10-31)
-------------------

- Add BLS types

v2.0.0 (2019-10-31)
-------------------

- Expose Type Hints as per PEP 561

v1.0.0 (2018-06-08)
-------------------

- Added annotations from ``py-evm``.

v0.3.1 (2018-06-07)
-------------------

- Removed ``eth-utils`` requirement.

v0.3.0 (2018-06-07)
-------------------

- Updated ``eth-utils`` requirement.

v0.2.0 (2018-06-07)
-------------------

- Launched repository, claimed names for pip, RTD, github, etc.
