# Copyright (C) 2020-2026 Motphys Technology Co., Ltd. All Rights Reserved.
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Motrix Forge.
#
# Motrix Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Motrix Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Motrix Forge. If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================


class Description:
    """Human-readable descriptions for MJCF element attributes.

    Stores documentation strings from the MJCF specification (mjcf_md).
    Each class attribute holds a description dict keyed by attribute name.

    Usage::

        tooltip = Description.JointDesc["Type"]
    """

    # ── Joint (body/joint) ──
    JointDesc = {
        "Element": (
            "This element creates a joint. A joint creates motion degrees of freedom between the "
            "body where it is defined and the body's parent. If multiple joints are defined in the "
            "same body, the corresponding spatial transformations are applied in order. If no "
            "joints are defined, the body is welded to its parent."
        ),
        "Name": "Name of the joint.",
        "Type": (
            "Type of the joint. The keywords have the following meaning: "
            'the free type creates a free "joint" with three translational and three rotational '
            "degrees of freedom making the body floating; the ball type creates a ball joint with "
            "three rotational degrees of freedom; the slide type creates a sliding or prismatic "
            "joint with one translational degree of freedom; the hinge type creates a hinge joint "
            "with one rotational degree of freedom. Choice: free, ball, slide, hinge."
        ),
        "Group": "Integer group for custom tags and visualization filtering.",
        "Pos": (
            "Position of the joint, specified in the frame of the body where the joint is defined. "
            "For free joints this attribute is ignored."
        ),
        "Axis": (
            "This attribute specifies the axis of rotation for hinge joints and the direction of "
            "translation for slide joints. It is ignored for free and ball joints. The vector "
            "specified here is automatically normalized to unit length as long as its length is "
            "greater than 10E-14; otherwise a compile error is generated."
        ),
        "Range": (
            "The joint limits. Limits can be imposed on all joint types except for free joints. "
            "For hinge and ball joints, the range is specified in degrees or radians depending on "
            "the angle attribute of the compiler element. For ball joints, the limit is imposed on "
            "the angle of rotation (relative to the reference configuration) regardless of the axis "
            "of rotation. Only the second range parameter is used for ball joints; the first range "
            "parameter should be set to 0."
        ),
        "Limited": (
            "This attribute specifies if the joint has limits. It interacts with the range attribute. "
            'If this attribute is "false", joint limits are disabled. If this attribute is "true", '
            'joint limits are enabled. If this attribute is "auto", and autolimits is set in the '
            "compiler element, joint limits will be enabled if range is defined. "
            "Choice: false, true, auto."
        ),
        "SpringDamper": (
            "When both numbers are positive, the compiler will override any stiffness and damping "
            "values specified with the attributes below, and will instead set them automatically "
            "so that the resulting mass-spring-damper for this joint has the desired time constant "
            "(first value) and damping ratio (second value). This is done by taking into account "
            "the joint inertia in the model reference configuration."
        ),
        "SolRefLimit": "Solver reference parameters for joint limits. See solver parameters.",
        "SolImpLimit": "Solver impedance parameters for joint limits. See solver parameters.",
        "SolRefFriction": "Solver reference parameters for joint friction.",
        "SolImpFriction": "Solver impedance parameters for joint friction.",
        "Stiffness": (
            "Joint stiffness. If this value is positive, a spring will be created with equilibrium "
            "position given by springref. The spring force is computed along with the other "
            "passive forces."
        ),
        "SpringRef": (
            "The joint position or angle in which the joint spring (if any) achieves equilibrium. "
            "All spring reference values specified with this attribute are collected into the spring "
            "reference configuration, which is also used to compute the spring reference lengths "
            "of all tendons."
        ),
        "Armature": (
            "Additional inertia associated with movement of the joint that is not due to body mass. "
            "This added inertia is usually due to a rotor (a.k.a armature) spinning faster than "
            "the joint itself due to a geared transmission. Positive armature significantly "
            "improves simulation stability, even for small values."
        ),
        "Damping": (
            "Damping applied to all degrees of freedom created by this joint. Unlike friction loss "
            "which is computed by the constraint solver, damping is simply a force linear in "
            "velocity. It is included in the passive forces."
        ),
        "FrictionLoss": (
            "Friction loss due to dry friction. This value is the same for all degrees of freedom "
            "created by this joint. To enable friction loss, set this attribute to a positive value."
        ),
        "Margin": (
            "The distance threshold below which limits become active. The constraint solver normally "
            "generates forces as soon as a constraint becomes active, even if the margin parameter "
            "makes that happen at a distance. This attribute together with solreflimit and "
            "solimplimit can be used to model a soft joint limit."
        ),
        "Ref": (
            "The reference position or angle of the joint. This attribute is only used for slide "
            "and hinge joints. It defines the joint value corresponding to the initial model "
            "configuration."
        ),
        "ActuatorFrcRange": (
            "Range for clamping total actuator forces acting on this joint. It is available only "
            "for scalar joints (hinge and slider) and ignored for ball and free joints. The "
            "compiler expects the first value to be smaller than the second value."
        ),
        "ActuatorFrcLimited": (
            "This attribute specifies whether actuator forces acting on the joint should be clamped. "
            "It is available only for scalar joints (hinge and slider) and ignored for ball and "
            "free joints. Choice: false, true, auto."
        ),
    }

    # ── Body (body) ──
    BodyDesc = {
        "Element": (
            "This element is used to construct the kinematic tree via nesting. The element "
            "worldbody is used for the top-level body, while the element body is used for all "
            "other bodies. Bodies form the nodes of the kinematic tree. Each body can have child "
            "bodies, joints, geoms, sites, cameras, and lights."
        ),
        "Name": "Name of the body.",
        "ChildClass": (
            "If this attribute is present, all descendant elements that admit a defaults class will "
            "use the class specified here, unless they specify their own class or another body or "
            "frame with a childclass attribute is encountered along the chain of nested bodies and "
            "frames."
        ),
        "Pos": "The 3D position of the body frame, in the parent coordinate frame.",
        "Mocap": (
            'If this attribute is "true", the body is labeled as a mocap body. This is allowed '
            "only for bodies that are children of the world body and have no joints. Such bodies "
            "are fixed from the viewpoint of the dynamics, but nevertheless the forward kinematics "
            "set their position and orientation via the mocap system at each time step."
        ),
        "GravComp": (
            "Gravity compensation force, specified as fraction of body weight. This attribute "
            "creates an upwards force applied to the body's center of mass, countering the force "
            "of gravity. A value of 1 creates an upward force equal to the body's weight and "
            "compensates for gravity exactly."
        ),
    }

    # ── Geom (body/geom) ──
    GeomDesc = {
        "Element": (
            "A geometric element attached rigidly to the body within which it is defined. "
            "Multiple geoms can be attached to the same body. At runtime they determine the "
            "appearance and collision properties of the body. At compile time they can also "
            "determine the inertial properties of the body."
        ),
        "Name": "Name of the geom.",
        "Type": (
            "Type of geometric shape. The plane type defines a plane which is infinite for "
            "collision detection purposes; it can only be attached to the world body or static "
            "children of the world. The sphere type defines a sphere centered at the geom's "
            "position, using one size parameter for the radius. The capsule type defines a "
            "capsule — a cylinder capped with two half-spheres — oriented along the Z axis "
            "of the geom's frame. The cylinder type defines a right circular cylinder oriented "
            "along the Z axis of the geom's frame. The box type defines a box whose half-sizes "
            "along X, Y and Z are given by the three size parameters. The mesh type defines a "
            "mesh referenced by the mesh attribute. The hfield type defines a height field "
            "referenced by the hfield attribute. "
            "Choice: plane, hfield, sphere, capsule, cylinder, box, ellipsoid, mesh."
        ),
        "Group": (
            "This attribute specifies an integer group to which the geom belongs. The only effect "
            "on the physics is at compile time, when body masses and inertias are inferred from "
            "geoms selected based on their group. At runtime this attribute is used by the "
            "visualizer to enable and disable the rendering of entire geom groups."
        ),
        "Contype": (
            "This attribute and conaffinity specify 32-bit integer bitmasks used for contact "
            "filtering of dynamically generated contact pairs. Two geoms can collide if the "
            "contype of one geom is compatible with the conaffinity of the other geom or vice "
            "versa. Compatible means that the two bitmasks have a common bit set to 1."
        ),
        "ConDim": (
            "The dimensionality of the contact space for a dynamically generated contact pair is "
            "set to the maximum of the condim values of the two participating geoms. The allowed "
            "values: 1 for frictionless contact; 3 for regular frictional contact opposing slip "
            "in the tangent plane; 4 for frictional contact opposing slip and rotation around "
            "the contact normal; 6 for frictional contact opposing slip, rotation around the "
            "contact normal, and rotation around the two axes of the tangent plane."
        ),
        "ConAffinity": "Bitmask for contact filtering; see contype above.",
        "Priority": (
            "The geom priority determines how the properties of two colliding geoms are combined "
            "to form the properties of the contact. When the priorities of the two geoms differ, "
            "the contact parameters of the higher-priority geom are used. When priorities are "
            "equal, the parameters are mixed according to solmix."
        ),
        "Size": (
            "Geom size parameters. The number of required parameters and their meaning depends on "
            "the geom type as documented under the type attribute. All required size parameters "
            "must be positive."
        ),
        "Material": (
            "If specified, this attribute applies a material to the geom. The material determines "
            "the visual properties of the geom. The only exception is color: if the rgba attribute "
            "is different from its internal default, rgba takes precedence while the remaining "
            "material properties are still applied."
        ),
        "RGBA": (
            "Instead of creating material assets and referencing them, this attribute can be used "
            "to set color and transparency only. This is not as flexible as the material mechanism, "
            "but is more convenient and is often sufficient. If the value of this attribute is "
            "different from the internal default, it takes precedence over the material."
        ),
        "Friction": (
            "Contact friction parameters for dynamically generated contact pairs. The first number "
            "is the sliding friction, acting along both axes of the tangent plane. The second "
            "number is the torsional friction, acting around the contact normal. The third number "
            "is the rolling friction, acting around both axes of the tangent plane. The friction "
            "parameters for the contact pair are combined depending on the solmix and priority "
            "attributes."
        ),
        "Mass": (
            "If this attribute is specified, the density attribute below is ignored and the geom "
            "density is computed from the given mass, using the geom shape and the assumption of "
            "uniform density. The computed density is then used to obtain the geom inertia."
        ),
        "Density": (
            "Material density used to compute the geom mass and inertia. The computation is based "
            "on the geom shape and the assumption of uniform density. This attribute is used only "
            "when the mass attribute above is unspecified."
        ),
        "Margin": (
            "Distance threshold below which contacts are detected and included in the global array the contact data."
        ),
        "Gap": (
            "This attribute is used to enable the generation of inactive contacts, i.e., contacts "
            "that are ignored by the constraint solver but are included in the contact data for "
            "the purpose of custom computations."
        ),
        "SolMix": (
            "This attribute specifies the weight used for averaging of contact parameters, and "
            "interacts with the priority attribute. When two geoms with equal priority collide, "
            "their contact parameters are mixed using solmix as the weight for one geom and "
            "(1 - solmix) for the other."
        ),
        "SolRef": "Solver reference parameters for contact simulation. See solver parameters.",
        "SolImp": "Solver impedance parameters for contact simulation. See solver parameters.",
    }

    # ── Site (body/site) ──
    SiteDesc = {
        "Element": (
            "A site is a simplified and restricted kind of geom. Semantically, sites represent "
            "locations of interest relative to the body frames. Sites do not participate in "
            "collisions and computation of body masses and inertias. However, sites can be used "
            "for mounting sensors, specifying via-points of spatial tendons, and constructing "
            "slider-crank transmissions for actuators."
        ),
        "Name": "Name of the site.",
        "Type": (
            "Type of geometric shape. This is used for rendering, and also determines the active "
            "sensor zone for touch sensors. Choice: sphere, capsule, cylinder, box."
        ),
        "Group": (
            "Integer group to which the site belongs. This attribute can be used for custom tags. "
            "It is also used by the visualizer to enable and disable the rendering of entire "
            "groups of sites."
        ),
        "Size": "Sizes of the geometric shape representing the site.",
        "Material": "Material used to specify the visual properties of the site.",
        "RGBA": (
            "Color and transparency. If this value is different from the internal default, it "
            "overrides the corresponding material properties."
        ),
        "Pos": "Position of the site frame.",
        "FromTo": (
            "This attribute can only be used with capsule, cylinder, ellipsoid and box sites. It "
            "provides an alternative specification of the site length as well as the frame "
            "position and orientation. The six numbers are the 3D coordinates of one point "
            "followed by the 3D coordinates of another point."
        ),
    }

    # ── Inertial (body/inertial) ──
    InertialDesc = {
        "Element": (
            "This element specifies the mass and inertial properties of the body. If this element "
            "is not included in a given body, the inertial properties are inferred from the geoms "
            "attached to the body. The inertial frame is such that its center coincides with the "
            "center of mass of the body, and its axes coincide with the principal axes of inertia."
        ),
        "Pos": (
            "Position of the inertial frame. This attribute is required even when the inertial "
            "properties can be inferred from geoms."
        ),
        "Mass": "Mass of the body. Negative values are not allowed.",
        "DiagInertia": ("Diagonal inertia matrix, expressing the body inertia relative to the inertial frame."),
        "FullInertia": (
            "Full inertia matrix M about the center of mass, expressed in link axes. "
            "Since M is 3-by-3 and symmetric, it is specified using only "
            "6 numbers in the following order: M(1,1), M(2,2), M(3,3), M(1,2), M(1,3), M(2,3)."
        ),
    }

    # ── Camera (body/camera) ──
    CameraDesc = {
        "Element": (
            "This element creates a camera, which moves with the body where it is defined. "
            "To create a fixed camera, define it in the world body. The camera is looking along "
            "the -Z axis of its frame; the +X axis points to the right, and the +Y axis points up."
        ),
        "Name": "Name of the camera.",
        "Mode": (
            "This attribute specifies how the camera position and orientation in world coordinates "
            'are computed in forward kinematics. "fixed" means that the position and orientation '
            'are fixed relative to the body where the camera is defined. "track" means that the '
            "camera position is at a constant offset from the body in world coordinates, while the "
            'camera orientation is constant in world coordinates. "trackcom" is similar to '
            '"track" but the constant spatial offset is defined relative to the center of mass of '
            'the kinematic subtree. "targetbody" means that the camera position is fixed in the '
            "body frame, while the camera orientation is adjusted so that it always points towards "
            'the targeted body. "targetbodycom" is the same as "targetbody" but the camera is '
            "oriented towards the center of mass of the subtree starting at the target body. "
            "Choice: fixed, track, trackcom, targetbody, targetbodycom."
        ),
        "Target": (
            'When the camera mode is "targetbody" or "targetbodycom", this attribute becomes '
            "required. It specifies which body should be targeted by the camera."
        ),
        "Type": ("Type of camera projection. Choice: perspective, orthographic."),
        "Fovy": (
            "Vertical field-of-view of the camera. If the camera uses a perspective projection, "
            "the field-of-view is expressed in degrees. If the camera uses an orthographic "
            "projection, the field-of-view is expressed in units of length."
        ),
        "Resolution": "Resolution of the camera in pixels (width, height).",
        "Pos": "Position of the camera frame.",
    }

    # ── Light (body/light) ──
    LightDesc = {
        "Element": (
            "This element creates a light, which moves with the body where it is defined. "
            "To create a fixed light, define it in the world body. Lights shine along the "
            "direction specified by the dir attribute."
        ),
        "Name": "Name of the light.",
        "Mode": (
            "This attribute specifies how the light position and orientation in world coordinates "
            'are computed in forward kinematics. "fixed" means that the position and orientation '
            'are fixed relative to the body. "track" means that the light position is at a '
            'constant offset from the body in world coordinates. "trackcom" is similar to '
            '"track" but the offset is relative to the center of mass. "targetbody" means that '
            "the light orientation is adjusted so that it always points towards the targeted body. "
            '"targetbodycom" is the same but oriented towards the center of mass of the target '
            "body. Choice: fixed, track, trackcom, targetbody, targetbodycom."
        ),
        "Target": ('This attribute specifies which body should be targeted in "targetbody" and "targetbodycom" modes.'),
        "Type": (
            "Determines the type of light. The built-in renderer supports spot, point and "
            "directional lights. Choice: spot, point, directional."
        ),
        "Dir": "Direction of the light.",
        "Pos": "Position of the light.",
        "Cutoff": ("Cutoff angle for spotlights, always in degrees regardless of the global angle setting."),
        "Range": (
            "The effective range of the light. Objects further than this distance from the light "
            "position will not be illuminated by this light. This only applies to spotlights."
        ),
        "Attenuation": (
            "The constant, linear and quadratic attenuation coefficients for Phong lighting. "
            "The default corresponds to no attenuation."
        ),
        "Intensity": (
            "The intensity of the light source, measured in candela, used for physically-based lighting models."
        ),
        "Ambient": ("The ambient color of the light, used by the default Phong lighting model."),
        "Diffuse": (
            "The color of the light. For the Phong (default) lighting model, this defines the "
            "diffuse color of the light."
        ),
        "Specular": ("The specular color of the light, used by the default Phong lighting model."),
        "CastShadow": ('If this attribute is "true" the light will cast shadows.'),
        "BulbRadius": ("The radius of the light source which can affect shadow softness depending on the renderer."),
    }

    # ── Actuator (common attributes for all actuator types) ──
    ActuatorDesc = {
        "Element": (
            "Actuators convert control signals into forces acting on joints, tendons, or directly "
            "on bodies. Each actuator type combines independently configurable subsystems: "
            "activation dynamics, gain, and bias."
        ),
        "Name": "Element name.",
        "Target": "Target object for the actuator to control.",
        "Group": (
            "Integer group to which the actuator belongs. This attribute can be used for custom "
            "tags. It is also used by the visualizer to enable and disable the rendering of "
            "entire groups of actuators."
        ),
        "CtrlLimited": (
            "If true, the control input to this actuator is automatically clamped to ctrlrange at "
            'runtime. If false, control input clamping is disabled. If "auto" and autolimits is '
            "set in compiler, control clamping will automatically be set to true if ctrlrange is "
            "defined. Choice: false, true, auto."
        ),
        "ForceLimited": (
            "If true, the force output of this actuator is automatically clamped to forcerange at "
            'runtime. If false, force clamping is disabled. If "auto" and autolimits is set in '
            "compiler, force clamping will automatically be set to true if forcerange is defined. "
            "Choice: false, true, auto."
        ),
        "CtrlRange": (
            "Range for clamping the control input. The first value must be smaller than the second "
            "value. Setting this attribute without specifying ctrllimited is an error if autolimits "
            'is "false" in compiler.'
        ),
        "ForceRange": (
            "Range for clamping the force output. The first value must be no greater than the "
            "second value. Setting this attribute without specifying forcelimited is an error if "
            'autolimits is "false" in compiler.'
        ),
        "Gear": (
            "Scales the length (and consequently moment arms, velocity and force) of the actuator, "
            "for all transmission types. It is different from the gain in the force generation "
            "mechanism, because the gain only scales the force output and does not affect the "
            "length, moment arms and velocity. For actuators with scalar transmission, only the "
            "first element of this vector is used."
        ),
        "Joint": (
            "If specified, the actuator acts on the given joint. For hinge and slide joints, the "
            "actuator length equals the joint position/angle times the first element of gear. "
            "For ball joints, the first three elements of gear define a 3D rotation axis in the "
            "child frame around which the actuator produces torque."
        ),
        "Tendon": (
            "If specified, the actuator acts on the given tendon. The actuator length equals the "
            "tendon length times the gear ratio."
        ),
        "Type": "Type of the actuator. Choice: general, motor, position, velocity, adhesion.",
        "TargetType": "Type of the target object (joint, tendon, link, site).",
        "Kp": (
            "Position feedback gain. Used internally as gainprm[0] and also negated into "
            "biasprm[1] to produce a restoring force proportional to position error."
        ),
        "Kv": (
            "Velocity feedback gain. Used internally as gainprm[0] and also negated into "
            "biasprm[2] to produce a damping force proportional to velocity."
        ),
        "Gain": (
            "Gain of the actuator, in units of force per unit of control. The force output is "
            "the control value multiplied by the gain."
        ),
        "GainType": (
            "The gain type determines the gain_term in the force generation formula. Available "
            "types are: fixed (gain_term = gainprm[0]), affine (gain_term = gainprm[0] + "
            "gainprm[1]*length + gainprm[2]*velocity). Choice: fixed, affine, muscle, user."
        ),
        "BiasType": (
            "The bias type determines the bias_term in the force generation formula. Available "
            "types are: none (bias_term = 0), affine (bias_term = biasprm[0] + biasprm[1]*length "
            "+ biasprm[2]*velocity). Choice: none, affine, muscle, user."
        ),
        "DynPrm": (
            "Activation dynamics parameters. The built-in activation types (except for muscle) use "
            "only the first parameter, but additional parameters are provided in case user "
            "callbacks implement a more elaborate model."
        ),
        "GainPrm": (
            "Gain parameters. The built-in gain types (except for muscle) use only the first "
            "parameter, but additional parameters are provided in case user callbacks implement a "
            "more elaborate model."
        ),
        "BiasPrm": ("Bias parameters. The affine bias type uses three parameters."),
        "InheritRange": (
            "Automatically sets the actuator's ctrlrange to match the transmission target's range. "
            "A positive value X sets the ctrlrange around the midpoint of the target range, scaled "
            "by X. This attribute is exclusive with ctrlrange and available only for joint and "
            "tendon transmissions which have range defined."
        ),
    }

    # ── Equality ──
    EqualityDesc = {
        "Element": (
            "Equality constraints impose mathematical relationships between positions or "
            "velocities of different parts of the model. Three types are supported: connect "
            "(ball joint outside the kinematic tree), weld (rigid attachment), and joint "
            "(quartic polynomial relationship between two scalar joints)."
        ),
        "Name": "Name of the equality constraint.",
        "Active": (
            'If this attribute is set to "true", the constraint is active and the constraint '
            "solver will try to enforce it."
        ),
        "Type": "Type of equality constraint (connect, weld, joint).",
        "TargetType": "Type of the target objects in the equality constraint.",
        "SolRef": "Solver reference parameters for equality constraints. See solver parameters.",
        "SolImp": "Solver impedance parameters for equality constraints. See solver parameters.",
        "Body1": "Name of the first body participating in the constraint.",
        "Body2": (
            "Name of the second body participating in the constraint. If this attribute is omitted, "
            "the second body is the world body."
        ),
        "Anchor": "Coordinates of the 3D anchor point where the two bodies are connected.",
        "Site1": "Name of a site belonging to the first body participating in the constraint.",
        "Site2": "Name of a site belonging to the second body participating in the constraint.",
        "Joint1": "Name of the first joint.",
        "Joint2": ("Name of the second joint. If this attribute is omitted, the first joint is fixed to a constant."),
        "PolyCoef": (
            "Coefficients a0 through a4 of the quartic polynomial relating the positions of joint1 and joint2."
        ),
        "RelPose": (
            "This attribute specifies the relative pose (3D position followed by 4D quaternion "
            "orientation) of body2 relative to body1."
        ),
        "TorqueScale": (
            "A constant that scales the angular residual (angular constraint violation). This "
            "value has units of length and can be understood as the diameter of a flat patch of "
            "glue sticking the two bodies together."
        ),
    }

    # ── Tendon (tendon/fixed) ──
    TendonDesc = {
        "Element": (
            "Tendons can be used to impose length limits, simulate spring, damping and dry "
            "friction forces, as well as attach actuators to them. The fixed tendon length is "
            "defined as a linear combination of joint positions."
        ),
        "Name": "Name of the tendon.",
        "Type": "Type of the tendon (fixed).",
        "Targets": "List of target sites along the tendon path.",
        "Group": "Integer group to which the tendon belongs.",
        "Limited": (
            'If this attribute is "true", the length limits defined by the range attribute are '
            "imposed by the constraint solver. Choice: false, true, auto."
        ),
        "Range": "Range of allowed tendon lengths.",
        "SolRefLimit": "Solver reference parameters for tendon limits. See solver parameters.",
        "SolImpLimit": "Solver impedance parameters for tendon limits. See solver parameters.",
        "SpringLength": (
            "Spring resting position. If one value is given, it corresponds to the length of the "
            "tendon at rest. If it is -1, the tendon resting length is determined from the model "
            "reference configuration. If two non-decreasing values are given, they define a "
            "dead-band range."
        ),
        "Stiffness": (
            "Stiffness coefficient. A positive value generates a spring force (linear in position) "
            "acting along the tendon."
        ),
        "Damping": (
            "Damping coefficient. A positive value generates a damping force (linear in velocity) "
            "acting along the tendon."
        ),
        "FrictionLoss": (
            "Friction loss caused by dry friction. To enable friction loss, set this attribute to a positive value."
        ),
        "Margin": (
            "The limit constraint becomes active when the absolute value of the difference between "
            "the tendon length and either limit of the specified range falls below this margin."
        ),
        "Width": "Radius of the cross-section area of the tendon, used for rendering.",
        "RGBA": "Color and transparency of the tendon.",
    }

    # ── Tendon Target (tendon/fixed/joint) ──
    TendonTargetDesc = {
        "Element": (
            "A joint contributing to the length computation of a fixed tendon. The position or "
            "angle of each included joint is multiplied by the corresponding coef value, and "
            "added up to obtain the tendon length."
        ),
        "Target": "Target site object for the tendon path.",
        "Joint": (
            "Name of the joint to be added to the fixed tendon. Only scalar joints (slide and "
            "hinge) can be referenced here."
        ),
        "Coef": ("Scalar coefficient multiplying the position or angle of the specified target."),
    }

    # ── Contact (contact/exclude, contact/pair) ──
    ContactDesc = {
        "Element": (
            "This element is used to exclude a pair of bodies from collision checking. "
            "Collisions between any geom defined in the first body and any geom defined in "
            "the second body are excluded."
        ),
        "Name": "Name of this contact (exclude, pair).",
        "Type": "Type of the contact definition (exclude, pair).",
        "Target1": "The name of the first body/geom in the (exclude, pair).",
        "Target2": "The name of the second body/geom in the (exclude, pair).",
        "Condim": (
            "The dimensionality of the contacts generated by this geom pair. "
            "Allowed values: 1 for frictionless contact; 3 for regular frictional contact; "
            "4 for frictional contact opposing slip and rotation around the contact normal; "
            "6 for frictional contact opposing slip, rotation around the contact normal, "
            "and rotation around the two axes of the tangent plane."
        ),
        "Friction": (
            "The friction coefficients of the contacts generated by this geom pair. "
            "Making the first two coefficients different results in anisotropic tangential "
            "friction. Making the last two coefficients different results in anisotropic "
            "rolling friction."
        ),
        "SolRef": "Solver reference parameters for contact simulation. See solver parameters.",
        "SolRefFriction": (
            "Solver reference parameters for friction dimensions. The default value of "
            '(0, 0) means "use the same values as solref", and this attribute only takes '
            "effect for elliptic friction cones."
        ),
        "Margin": (
            "Distance threshold below which contacts are detected and included in the global array the contact data."
        ),
        "Gap": (
            "Used to enable the generation of inactive contacts, i.e., contacts that are "
            "ignored by the constraint solver but are included in the contact data for "
            "the purpose of custom computations."
        ),
    }

    # ── Compiler ──
    CompilerDesc = {
        "Element": (
            "This element is used to set options for the built-in parser and compiler. After "
            "parsing and compilation it no longer has any effect. The settings here are global "
            "and apply to the entire model."
        ),
        "AutoLimits": (
            'If "true", attributes such as "limited", "forcelimited", "ctrllimited", and '
            '"actlimited" are unnecessary and their value will be inferred from the presence of '
            'their corresponding "range" attribute. If "false", no such inference will happen.'
        ),
        "Angle": (
            "This attribute specifies whether the angles in the MJCF model are expressed in units "
            "of degrees or radians. The compiler converts degrees into radians internally. "
            "Choice: radian, degree."
        ),
        "EulerSeq": (
            "This attribute specifies the sequence of Euler rotations for all euler attributes of "
            "elements that have spatial frames. This must be a string with exactly 3 characters "
            "from the set {x, y, z, X, Y, Z}. "
            "Choice: zyx, zxy, yxz, yzx, xyz, xzy."
        ),
        "AssetDir": "This attribute sets the values of both meshdir and texturedir.",
        "MeshDir": ("This attribute instructs the compiler where to look for mesh and height field files."),
        "TextureDir": ("This attribute is used to instruct the compiler where to look for texture files."),
    }

    # ── Visual (visual/global, visual/headlight, visual/map, visual/rgba) ──
    VisualDesc = {
        "Element": (
            "Settings that affect the visualizer. The settings here are global, in contrast "
            "with the element-specific visual settings. Some global settings affect properties "
            "such as triangulation of geometric primitives that cannot be set per element."
        ),
        "Fovy": "Vertical field of view of the free camera, in degrees if using perspective projection.",
        "Azimuth": "Azimuth angle of the free camera.",
        "Elevation": "Elevation angle of the free camera.",
        "Orthographic": "Use orthographic projection instead of perspective.",
        "Ambient": "Ambient light color.",
        "Diffuse": "Diffuse light color.",
        "Specular": "Specular light color.",
        "Active": "Whether headlight is active.",
        "FogStart": "Distance to the start of the fog effect.",
        "FogEnd": "Distance to the end of the fog effect.",
        "ZNear": "Distance to the near clipping plane.",
        "ZFar": "Distance to the far clipping plane.",
        "Haze": "Haze color.",
        "Fog": "Fog color.",
        "Joint": "Joint highlight color.",
        "BV": "Bounding volume color.",
        "ContactForce": "Color of the arrows used to render contact forces.",
    }

    # ── Quality (visual/quality) ──
    QualityDesc = {
        "Element": (
            "Settings that affect the quality of rendering. "
            "Larger values result in higher quality but possibly slower speed."
        ),
        "ShadowSize": (
            "This attribute specifies the size of the square texture used for directional "
            "and spot light shadow mapping. Higher values result in smoother shadows."
        ),
        "PointShadowSize": (
            "This attribute specifies the size of the square texture used for point light "
            "shadow mapping. Higher values result in smoother shadows."
        ),
    }

    # ── Tonemapping (visual/tonemapping) ──
    TonemappingDesc = {
        "Element": ("Tonemapping settings. Controls the tonemapping method applied during rendering."),
        "Method": (
            "The tonemapping method to apply during rendering. "
            '"none" means no tonemapping is applied. '
            '"aces" applies the ACES (Academy Color Encoding System) tonemapping. '
            "Choice: none, aces."
        ),
    }

    # ── SSGI (visual/ssgi) ──
    SsgiDesc = {
        "Element": (
            "Screen-space global illumination (SSGI) settings. Controls SSGI post-processing effect in the visualizer."
        ),
        "Active": "Whether SSGI post-processing is active.",
        "ResolutionScale": (
            "Control the quality of the fast GI lighting. "
            "Higher resolution scale uses less memory (buffer size = 1 / resolutionscale). "
            "Value in 1, 2, 4; input other value will set to 2."
        ),
        "RayCount": "Amount of GI ray to trace for each pixel.",
        "StepCount": "Amount of screen sample per GI ray.",
        "Thickness": (
            "Geometric thickness of the surfaces when computing fast GI and ambient occlusion. "
            "Reduces light leaking and missing contact occlusion."
        ),
        "Intensity": "GI intensity.",
        "GiDenoiseOffset": "GI denoise pixel offset size, 0 means no denoise.",
        "RRayCount": "Amount of screen sample per reflection ray.",
        "RDenoiseOffset": "Reflection denoise pixel offset size, 0 means no denoise.",
    }

    # ── Sensor ──
    SensorDesc = {
        "Element": (
            "Sensors output scalar, vector, or matrix quantities at each time step. "
            "They are configured by specifying the sensor type and the target object "
            "(site, joint, body, etc.) whose properties are being measured."
        ),
        "Name": "Name of the sensor.",
        "Type": (
            "Type of sensor measurement. "
            "Choice: Jointpos, Jointvel, Touch, Accelerometer, Velocimeter, Gyro, Framepos, "
            "Framequat, Framexaxis, Frameyaxis, Framezaxis, Framelinvel, Frameangvel, "
            "Subtreecom, Subtreelinvel, Subtreeangmom, Contact."
        ),
        "Target": "Target object for the sensor measurement.",
        "TargetType": "Type of the target object (body, xbody, geom, site, joint, camera).",
        "Ref": "Reference object for relative sensor measurements.",
        "RefType": "Type of the reference object.",
        "Noise": "Noise level of the sensor.",
        "Cutoff": "Cutoff frequency of the sensor filter.",
        "Num": (
            "The maximum number of contacts to detect and report. When more contacts "
            "are found than this value, only the first contacts (up to this limit) are "
            "used, unless a reduction method is specified."
        ),
        "Data": (
            "The type or types of contact data to report in the sensor output. "
            "Multiple data types may be listed in sequence. "
            "Available types: found, force, torque, distance, pos, normal, tangent."
        ),
        "Reduce": (
            "The method used to reduce multiple contacts to a single output value. "
            "Choice: none, mindist, maxforce, netforce."
        ),
    }

    # ── Attach ──
    AttachDesc = {
        "Element": (
            "The attach element is used to attach an external MJCF model's body subtree to "
            "the current body. This is useful for modular model composition. Unlike include "
            "which merges the entire external model at the root level, attach inserts a "
            "specific body's children into the current body hierarchy."
        ),
        "Model": "The model defined in asset element.",
        "File": "File path to the external model.",
        "Body": "Name of the body in the sub-model to attach here. None means attaching the whole world body.",
        "Prefix": "Prefix to prepend to all names in the sub-model.",
    }

    # ── Replicate ──
    ReplicateDesc = {
        "Element": (
            "This element is used to replicate a sub-tree of the model. The children of "
            "the replicate element are repeated count times with configurable translation "
            "and rotation offsets."
        ),
        "Count": "Number of times to replicate the child nodes.",
        "Sep": "Separator used to generate new names for the replicated elements.",
        "Offset": "Translation offset between consecutive replications.",
        "Euler": "Rotation offset between consecutive replications.",
    }

    # ── Option (option) ──
    OptionDesc = {
        "Element": (
            "Global simulation options that control physics behavior and solver settings. "
            "These are simulation options and do not affect the compilation process in any way; "
            "they are simply copied into the low level model."
        ),
        "TimeStep": (
            "The simulation time step in seconds. This is the single most important parameter "
            "affecting the speed-accuracy trade-off which is inherent in every physics simulation. "
            "Smaller values result in better accuracy and stability. To achieve real-time performance, "
            "the time step must be larger than the CPU time per step. Models with many floating "
            "objects (resulting in many contacts) are more demanding computationally."
        ),
        "Gravity": (
            "Gravitational acceleration vector. In the default world orientation the Z-axis points "
            "up, which is the convention used throughout the simulation stack and is not recommended "
            "to deviate from."
        ),
        "Iterations": (
            "Maximum number of iterations of the constraint solver. When the warmstart flag is "
            "enabled (which is the default), accurate results are obtained with fewer iterations. "
            "Larger and more complex systems with many interacting constraints require more iterations."
        ),
        "Tolerance": (
            "Tolerance threshold used for early termination of the iterative solver. For PGS, the "
            "threshold is applied to the cost improvement between two iterations. For CG and Newton, "
            "it is applied to the smaller of the cost improvement and the gradient norm. Set the "
            "tolerance to 0 to disable early termination."
        ),
        "OSolRef": (
            "These attributes replace the solref, solimp and friction parameters of all active "
            "contact pairs when contact override is enabled."
        ),
        "OSolImp": (
            "These attributes replace the solref, solimp and friction parameters of all active "
            "contact pairs when contact override is enabled."
        ),
        "OFriction": (
            "These attributes replace the solref, solimp and friction parameters of all active "
            "contact pairs when contact override is enabled."
        ),
        "OMargin": (
            "This attribute replaces the margin parameter of all active contact pairs when Contact "
            "override is enabled. Otherwise the element-specific margin attribute of geom or pair is "
            "used depending on how the contact pair was generated."
        ),
    }

    # ── Option Flag (option/flag) ──
    OptionFlagDesc = {
        "Element": (
            "Flags that enable and disable different parts of the simulation pipeline. "
            "The actual flags used at runtime are represented as the bits of two integers, "
            "used to disable standard features and enable optional features respectively."
        ),
        "Constraint": (
            "When set to disable, all standard computations related to the constraint solver are "
            "skipped and no constraint forces are applied. Note that the equality, frictionloss, "
            "limit, and contact flags each disable computations for a specific type of constraint; "
            "both this flag and the type-specific flag must be set to enable for a given computation "
            "to be performed. Choice: disable, enable."
        ),
        "Equality": (
            "When set to disable, all standard computations related to equality constraints are "
            "skipped. Choice: disable, enable."
        ),
        "FrictionLoss": (
            "When set to disable, all standard computations related to friction loss constraints "
            "are skipped. Choice: disable, enable."
        ),
        "Limit": (
            "When set to disable, all standard computations related to joint and tendon limit "
            "constraints are skipped. Choice: disable, enable."
        ),
        "Contact": (
            "When set to disable, collision detection and all standard computations related to "
            "contact constraints are skipped. Choice: disable, enable."
        ),
        "Gravity": (
            "When set to disable, the gravitational acceleration vector is replaced with (0 0 0) "
            "at runtime, without changing the stored value. Once the flag is re-enabled, the stored "
            "value is used again. Choice: disable, enable."
        ),
        "Actuation": (
            "When set to disable, all standard computations related to actuator forces are skipped, "
            "including the actuator dynamics. As a result, no actuator forces are applied to the "
            "simulation. Choice: disable, enable."
        ),
        "RefSafe": "Choice: disable, enable.",
        "Override": (
            "When set to enable, activates the Contact override mechanism, which causes the global "
            "o_margin, o_solref, o_solimp, and o_friction values to replace the corresponding "
            "per-contact parameters for all active contact pairs. Choice: disable, enable."
        ),
    }

    # ── Statistic ──
    StatisticDesc = {
        "Element": (
            "This element is used to override model statistics computed by the compiler. "
            "These statistics are not only informational but are also used to scale various "
            "components of the rendering and perturbation."
        ),
        "Extent": (
            "Replaces the extent value computed by the compiler. The computed value is half the side "
            "of the bounding box of the model in the initial configuration. At runtime this value is "
            "multiplied by some of the attributes of the map element. When the model is first loaded, "
            "the free camera's initial distance from the center is 1.5 times the extent. Must be "
            "strictly positive."
        ),
        "Center": (
            "Replaces the center value computed by the compiler. The computed value is the center of "
            "the bounding box of the entire model in the initial configuration. This 3D vector is "
            "used to center the view of the free camera when the model is first loaded."
        ),
    }

    # ── Include ──
    IncludeDesc = {
        "Element": (
            "Include an external MJCF file, merging its content at the point of inclusion. "
            "This enables modular model construction by referencing shared component files."
        ),
        "File": "Path to the external XML file to include.",
        "RawFile": "Path to the external raw data file to include.",
    }
