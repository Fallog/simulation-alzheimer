import numpy as np
from System import ReactionDiffusionAtmApoeSystem
from Space1D import SpatialSpace, TimeSpace
from Parameter import DiffusionParameter, TransportParameter, FragmentationParameter, PermeabilityParameter


def test_compute_dimers_next_density() -> bool:
    a_system = ReactionDiffusionAtmApoeSystem()
    a_spatial_space = SpatialSpace(5, 5)
    a_time_space = TimeSpace(1, 5)
    a_system.setup_spaces(a_spatial_space, a_time_space)

    a_monomers_initial_state = np.array([1.0, 1.2, 1.5, 1.2, 1.0])
    a_dimers_initial_state = np.array([2.0, 2.0, 2.0, 2.0, 2.0])
    a_apoe_initial_state = np.array([5.0, 0.0, 0.0, 0.0, 0.0])
    a_complexes_initial_state = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    a_system.setup_initial_population_conditions(a_monomers_initial_state, a_dimers_initial_state, a_apoe_initial_state,
                                                 a_complexes_initial_state)
    a_k = 0.5
    a_ka = 0.6
    a_diffusion = DiffusionParameter(1.1, 1.5)
    a_transport = TransportParameter(1.1, 3.0)
    a_fragmentation = FragmentationParameter(1.1, 1.5, 3.0)
    a_fragmentation.setup_values_over_time(a_time_space)
    a_permeability = PermeabilityParameter(2.8, 1, 2.5)
    a_ratio_fragmentation = 1.3

    a_system.setup_parameters(a_k, a_ka, a_diffusion, a_transport, a_fragmentation, a_permeability,
                              a_ratio_fragmentation)

    a_time_index = 2

    a_system.compute_dimers_next_density(a_time_index)

    expected_dimers_values = np.array([1.3475, 1.36, 1.37875, 1.36, 1.3475])

    return np.allclose(a_system.dimers.next_values, expected_dimers_values)


def test_compute_apoe_next_density() -> bool:
    a_system = ReactionDiffusionAtmApoeSystem()
    a_spatial_space = SpatialSpace(5, 5)
    a_time_space = TimeSpace(1, 5)
    a_system.setup_spaces(a_spatial_space, a_time_space)

    a_monomers_initial_state = np.array([1.0, 1.2, 1.5, 1.2, 1.0])
    a_dimers_initial_state = np.array([2.0, 2.0, 2.0, 2.0, 2.0])
    a_apoe_initial_state = np.array([5.0, 0.0, 0.0, 0.0, 0.0])
    a_complexes_initial_state = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    a_system.setup_initial_population_conditions(a_monomers_initial_state, a_dimers_initial_state, a_apoe_initial_state,
                                                 a_complexes_initial_state)
    a_k = 0.5
    a_ka = 0.6
    a_diffusion = DiffusionParameter(1.1, 1.5)
    a_transport = TransportParameter(1.1, 3.0)
    a_fragmentation = FragmentationParameter(1.1, 1.5, 3.0)
    a_fragmentation.setup_values_over_time(a_time_space)
    a_permeability = PermeabilityParameter(2.8, 1, 2.5)
    a_ratio_fragmentation = 1.3

    a_system.setup_parameters(a_k, a_ka, a_diffusion, a_transport, a_fragmentation, a_permeability,
                              a_ratio_fragmentation)

    a_time_index = 2

    a_system.compute_apoe_next_density(a_time_index)

    expected_apoe_values = np.array([4.25, 0., 0., 0., 0.])

    return np.array_equal(a_system.apoe_proteins.next_values, expected_apoe_values)


def test_compute_complexes_next_density() -> bool:
    a_system = ReactionDiffusionAtmApoeSystem()
    a_spatial_space = SpatialSpace(5, 5)
    a_time_space = TimeSpace(1, 5)
    a_system.setup_spaces(a_spatial_space, a_time_space)

    a_monomers_initial_state = np.array([1.0, 1.2, 1.5, 1.2, 1.0])
    a_dimers_initial_state = np.array([2.0, 2.0, 2.0, 2.0, 2.0])
    a_apoe_initial_state = np.array([5.0, 0.0, 0.0, 0.0, 0.0])
    a_complexes_initial_state = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    a_system.setup_initial_population_conditions(a_monomers_initial_state, a_dimers_initial_state, a_apoe_initial_state,
                                                 a_complexes_initial_state)
    a_k = 0.5
    a_ka = 0.6
    a_diffusion = DiffusionParameter(1.1, 1.5)
    a_transport = TransportParameter(1.1, 3.0)
    a_fragmentation = FragmentationParameter(1.1, 1.5, 3.0)
    a_fragmentation.setup_values_over_time(a_time_space)
    a_permeability = PermeabilityParameter(2.8, 1, 2.5)
    a_ratio_fragmentation = 1.3

    a_system.setup_parameters(a_k, a_ka, a_diffusion, a_transport, a_fragmentation, a_permeability,
                              a_ratio_fragmentation)

    a_time_index = 2

    a_system.compute_complexes_next_density(a_time_index)

    expected_complexes_values = np.array([0.75, 0., 0., 0., 0.])

    return np.array_equal(a_system.complexes.next_values, expected_complexes_values)


if __name__ == "__main__":
    assert test_compute_dimers_next_density()
    assert test_compute_apoe_next_density()
    assert test_compute_complexes_next_density()
