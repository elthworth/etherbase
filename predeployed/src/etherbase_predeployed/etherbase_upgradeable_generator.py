'''Module for generaration of Etherbase predeployed smart contract'''
from typing import Dict

from predeployed_generator.upgradeable_contract_generator import UpgradeableContractGenerator

from etherbase_predeployed.etherbase_generator import EtherbaseGenerator


class EtherbaseUpgradeableGenerator(EtherbaseGenerator):
    '''Generates non upgradeable instance of EtherbaseUpgradeable
    '''

    ARTIFACT_FILENAME = 'EtherbaseUpgradeable.json'

    # --------------- storage ---------------
    # ------------ Initializable ------------
    # 0:    _initialized, _initializing
    # --------- ContextUpgradeable ----------
    # 1:    __gap
    # ...   __gap
    # 50:   __gap
    # ---------- ERC165Upgradeable ----------
    # 51:   __gap
    # ...   __gap
    # 100:  __gap
    # ------- AccessControlUpgradeable -------
    # 101:  _roles
    # 102:  __gap
    # ...   __gap
    # 150:  __gap
    # -- AccessControlEnumerableUpgradeable --
    # 151:  _roleMembers
    # 152:  __gap
    # ...   __gap
    # 200:  __gap
    # --------- EtherbaseUpgradeable ---------


    INITIALIZED_SLOT = 0
    ROLES_SLOT = 101
    ROLE_MEMBERS_SLOT = 151

    @classmethod
    def generate_storage(cls, **kwargs) -> Dict[str, str]:
        '''Generate smart contract storage.

        Arguments:
            - schain_owner

        Returns an object in format:
        {
            "0x00": "0x5",
            "0x01": "0x13"
        }
        '''

        storage = super().generate_storage(**kwargs)
        cls._write_uint256(storage, cls.INITIALIZED_SLOT, 1)
        return storage


class UpgradeableEtherbaseUpgradeableGenerator(UpgradeableContractGenerator):
    '''Generates upgradeable instance of EtherbaseUpgradeable
    '''

    def __init__(self):
        super().__init__(implementation_generator=EtherbaseUpgradeableGenerator())
