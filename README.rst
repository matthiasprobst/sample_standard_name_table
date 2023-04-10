Sample Standard Name Table
==========================


|version v1| |project h5rdmtoolbox| |example|

.. |version v1| image:: https://img.shields.io/badge/version-v1-green.svg
.. |project h5rdmtoolbox| image:: https://img.shields.io/badge/project-h5RDMtoolbox-orange.svg
.. |example| image:: https://img.shields.io/badge/status-example-yellow.svg
.. |example| image:: https://img.shields.io/badge/check-passed-green.svg

A sample standard name table as used in the h5RDMtoolbox. This is an **example** standard
name table and used for testing and demonstration purposes in the `h5RDMtoolbox` package.

A `manage.py` python file is provided to perform a check and to 
sort the table (stored as a yaml file). It is recommended to run the 
file `manage.py` before publishing the table. The below table 
shows the table. The table is also produced in the python file:

Table
-----
.. list-table:: Table of standard names
	:widths: 10, 10, 10
	:header-rows: 1

	* - Standard Name
	  - Canonical Units
	  - Description
	* - absolute_air_pressure
	  - Pa
	  - Pressure is force per unit area. Absolute air pressure is pressure deviation to a total vacuum.
	* - air_density
	  - kg/m**3
	  - Air density is defined as the mass of air divided by its volume.
	* - air_mass_flow_rate
	  - kg/s
	  - Air mass flow rate is the mass of air that passes a certain cross sectiont per unit time.
	* - air_temperature
	  - degC
	  - Air temperature is the bulk temperature of the air, not the surface (skin) temperature. (CF Conventions)
	* - ambient_air_temperature
	  - K
	  - Air temperature is the bulk temperature of the air, not the surface (skin) temperature. Ambient air temperature is the temperature of the surrounding air.
	* - ambient_static_air_pressure
	  - Pa
	  - Static air pressure is the amount of pressure exerted by air that is not moving. Ambient static air pressure is the static air pressure of the surrounding air.
	* - difference_of_dynamic_air_pressure
	  - Pa
	  - Dynamic air pressure is a measure for kinetic energy per unit volume of moving air. Difference of dynamic air pressure is the difference between dynamic air pressures of two points.
	* - difference_of_static_air_pressure
	  - Pa
	  - Static air pressure is the amount of pressure exerted by air that is not moving. Difference of static air pressure is the difference between static air pressures of two points.
	* - difference_of_total_air_pressure
	  - Pa
	  - Total air pressure is the sum of static and dynamic air pressure. Difference of total air pressure is the difference between total air pressures of two points.
	* - dynamic_air_pressure
	  - Pa
	  - Dynamic air pressure is a measure for kinetic energy per unit volume of moving air.
	* - dynamic_air_viscosity
	  - Pa*s
	  - Dynamic air viscosity indicates the resistance  of air towards deformation under shear stress. (https://doi.org/10.1016/B978-0-08-096949-7.00020-0)
	* - kinematic_air_viscosity
	  - m**2/s
	  - Dynamic air viscosity indicates the resistance  of air towards deformation under shear stress. Kinematic viscosity. Dynamic air viscosity divided by air denisity equals kinematic air viscosity. (https://doi.org/10.1016/B978-0-12-410461-7.00007-9)
	* - magnitude_of_air_velocity
	  - m/s
	  - Magnitude of the vector quantity velocity.
	* - relative_humidity
	  - 
	  - Relative humidity is a measure of the water vapor content of air.
	* - static_air_pressure
	  - Pa
	  - Static air pressure is the amount of pressure exerted by air that is not moving.
	* - time
	  - s
	  - Recording time since start of experiment.
	* - total_air_pressure
	  - Pa
	  - The sum of static_air_pressure and dynamic_air_pressure.
	* - turbulent_kinetic_energy
	  - m**2/s**2
	  - The kinetic energy per unit mass of a fluid.
	* - x_air_velocity
	  - m/s
	  - Velocity is a vector quantity. X indicates the component in x-axis direction.
	* - x_coordinate
	  - m
	  - Coordinate in x axis direction.
	* - x_derivative_of_x_air_velocity
	  - 1/s
	  - Derivative of x air velocity in x-axis direction.
	* - x_derivative_of_y_air_velocity
	  - 1/s
	  - Derivative of y air velocity in x-axis direction.
	* - x_derivative_of_z_air_velocity
	  - 1/s
	  - Derivative of z air velocity in x-axis direction.
	* - x_pixel_coordinate
	  - pixel
	  - Pixel coordinate in x-axis direction.
	* - y_air_velocity
	  - m/s
	  - Velocity is a vector quantity. Y indicates the component in z-axis direction.
	* - y_coordinate
	  - m
	  - Coordinate in y axis direction.
	* - y_derivative_of_x_air_velocity
	  - 1/s
	  - Derivative of  x air velocity in y-axis direction.
	* - y_derivative_of_y_air_velocity
	  - 1/s
	  - Derivative of y air velocity in y-axis direction.
	* - y_derivative_of_z_air_velocity
	  - 1/s
	  - Derivative of z air velocity in y-axis direction.
	* - y_pixel_coordinate
	  - pixel
	  - Pixel coordinate in y-axis direction.
	* - yx_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "yx" indicates the component in y-axis direction.
	* - yy_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "yy" indicates the component in y-axis direction.
	* - yz_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "yz" indicates the component in y-axis direction.
	* - z_air_velocity
	  - m/s
	  - Velocity is a vector quantity. Z indicates the component in y-axis direction.
	* - z_air_vorticity
	  - 1/s
	  - Vorticity is a vector quantity. Z indicates the component in z-axis direction.
	* - z_coordinate
	  - m
	  - Coordinate in z axis direction.
	* - z_derivative_of_x_air_velocity
	  - 1/s
	  - Derivative of x air velocity in z-axis direction.
	* - z_derivative_of_y_air_velocity
	  - 1/s
	  - Derivative of y air velocity in z-axis direction.
	* - z_derivative_of_z_air_velocity
	  - 1/s
	  - Derivative of z air velocity in z-axis direction.
	* - zx_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "zx" indicates the component in y-axis direction.
	* - zy_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "zy" indicates the component in y-axis direction.
	* - zz_air_reynolds_stress
	  - m**2/s**2
	  - Reynolds stress is a tensor quantity. "Air" indicates, that the Reynolds stress is calculated for air. "zz" indicates the component in y-axis direction.