from mev_inspect.schemas.classified_traces import (
    Classification,
    ClassifierSpec,
    Protocol,
)

COMPOUND_V2_SPECS = [
    ClassifierSpec(
        abi_name="CEther",
        protocol=Protocol.compound_v2,
        classifications={
            "liquidateBorrow(address,address)": Classification.liquidate,
        },
    ),
    ClassifierSpec(
        abi_name="CErc20",
        protocol=Protocol.compound_v2,
        classifications={
            "liquidateBorrow(address,uint256,address)": Classification.liquidate,
        },
    ),
]

COMPOUND_CLASSIFIER_SPECS = [
    *COMPOUND_V2_SPECS,
]