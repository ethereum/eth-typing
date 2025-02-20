Release Notes
=============

.. towncrier release notes start

eth-typing v5.2.0 (2025-02-20)
------------------------------

Features
~~~~~~~~

- Add Prague to ForkName enum (`#94 <https://github.com/ethereum/eth-typing/issues/94>`__)


eth-typing v5.1.0 (2025-01-08)
------------------------------

Features
~~~~~~~~

- Add py313 support, drop ``bumpmyversion`` in favor of ``bump-my-version`` (`#93 <https://github.com/ethereum/eth-typing/issues/93>`__)


eth-typing v5.0.1 (2024-10-14)
------------------------------

Bugfixes
~~~~~~~~

- ``ABIEvent`` should use ``ABIComponentIndexed`` instead of ``ABIComponent`` as the type for ``inputs``. (`#92 <https://github.com/ethereum/eth-typing/issues/92>`__)


eth-typing v5.0.0 (2024-08-14)
------------------------------

Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Run ``mypy`` locally rather than in a ``pre-commit`` container (`#90 <https://github.com/ethereum/eth-typing/issues/90>`__)


eth-typing v5.0.0-beta.3 (2024-06-27)
-------------------------------------

Features
~~~~~~~~

- Replace ``ABIFunctionInfo`` type with ``ABIElementInfo`` to encompass all ``ABIElement`` types. ``ABIElementInfo`` includes the function ``abi`` (``ABIElement``), ``selector`` (``HexStr``) and ``args`` (``Tuple``). (`#85 <https://github.com/ethereum/eth-typing/issues/85>`__)


Internal Changes - for eth-typing Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Cleanup references to ABI types that have been removed. (`#87 <https://github.com/ethereum/eth-typing/issues/87>`__)


eth-typing v5.0.0-beta.2 (2024-06-18)
-------------------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Updates all modules and types with docstrings. Docs are now generated through ``autodoc``. (`#81 <https://github.com/ethereum/eth-typing/issues/81>`__)


Features
~~~~~~~~

- Move `URI` type from EthPM module to networks. (`#65 <https://github.com/ethereum/eth-typing/issues/65>`__)


Removals
~~~~~~~~

- Remove types related to the EthPM module which has been removed from ``web3.py`` (`#65 <https://github.com/ethereum/eth-typing/issues/65>`__)
- Remove deprecated ABI types ``ABIEventComponent``, ``ABIEventParam``, ``ABIFunctionComponent``, ``ABIFunctionParam``. (`#82 <https://github.com/ethereum/eth-typing/issues/82>`__)


eth-typing v5.0.0-beta.1 (2024-06-17)
-------------------------------------

Breaking changes
~~~~~~~~~~~~~~~~

- Mark ABI types with optional attributes.

  * ``ABIFunction`` requires ``type`` and ``name`` but ``inputs`` and ``outputs`` are optional.
  * ``ABIEvent`` requires ``type`` and ``name`` but ``inputs`` and ``anonymous`` are optional.
  * All attributes of ``ABIFunctionInfo`` are required.
  * ``ABIFallback`` and ``ABIReceive`` now require the ``type`` attribute.
  * ``ABIConstructor`` requires a ``type`` but ``inputs`` are optional.
  * ``ABIError`` requires ``type`` and ``name`` but ``inputs`` is optional.
  * ``ABIComponent`` requires ``type`` and ``name`` but ``components`` may be omitted so that ``inputs`` may use either ``primitive`` or ``tuple`` types. (`#76 <https://github.com/ethereum/eth-typing/issues/76>`__) (`#79 <https://github.com/ethereum/eth-typing/issues/79>`__)


eth-typing v4.3.1 (2024-06-17)
------------------------------

Bugfixes
~~~~~~~~

- Update ``typing_extensions`` to ``4.5.0`` which supposrts ``deprecated`` decorator. (`#80 <https://github.com/ethereum/eth-typing/issues/80>`__)


eth-typing v4.3.0 (2024-06-10)
------------------------------

Deprecations
~~~~~~~~~~~~

- Mark ``EthPM`` types as deprecated in the docs. (`#67 <https://github.com/ethereum/eth-typing/issues/67>`__)
- Deprecated ``ABIEventComponent``, ``ABIEventParam``, ``ABIFunctionComponent`` and ``ABIFunctionParam`` for removal in v5. (`#74 <https://github.com/ethereum/eth-typing/issues/74>`__)


Features
~~~~~~~~

- Add ``ABIError`` TypedDict for ``ABI`` error messages and ``ABIComponent`` TypedDict for ``ABI`` type components. (`#73 <https://github.com/ethereum/eth-typing/issues/73>`__)
- ``ABIComponentIndexed`` now extends ``ABIComponent`` to support the ``indexed`` property. (`#74 <https://github.com/ethereum/eth-typing/issues/74>`__)
- Added ``ABIError``, ``ABIFallback`` and ``ABIReceive`` types to ``ABIFunctionInfo.abi`` types. ``ABICallable`` is now a type alias for ``Union[ABIFunctionInfo, ABIError, ABIFallback, ABIReceive]``. (`#77 <https://github.com/ethereum/eth-typing/issues/77>`__)


eth-typing v4.2.3 (2024-05-06)
------------------------------

Features
~~~~~~~~

- Update networks types with the latest. (`#72 <https://github.com/ethereum/eth-typing/issues/72>`__)


eth-typing v4.2.2 (2024-04-29)
------------------------------

Bugfixes
~~~~~~~~

- Fixes types that were incorrectly defined for ``ABI`` utils. (`#62 <https://github.com/ethereum/eth-typing/issues/62>`__)


Features
~~~~~~~~

- Update network type mappings. (`#70 <https://github.com/ethereum/eth-typing/issues/70>`__)


Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- `#68 <https://github.com/ethereum/eth-typing/issues/68>`__


eth-typing v4.2.1 (2024-04-16)
------------------------------

Bugfixes
~~~~~~~~

- Put back types used for `EthPM`: `ContractName`, `Manifest`, and `URI`. (`#64 <https://github.com/ethereum/eth-typing/issues/64>`__)


eth-typing v4.2.0 (2024-04-15)
------------------------------

Features
~~~~~~~~

- Add type definitions to represent contract ``ABI`` s. (`#61 <https://github.com/ethereum/eth-typing/issues/61>`__)


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
