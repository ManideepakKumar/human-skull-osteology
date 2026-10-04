import time


class SkullOsteologyExplorer:

    def __init__(self):

        # ============================================================
        # MEMORIAL
        # ============================================================

        self.memorial = {
            "Name": "Dr. Kasakurthi Jagadeesh Babu",
            "Profession": "Neurosurgeon",
            "Associated With": "Mamata Hospital, Khammam",
            "Date": "September 2026",
            "Tribute": (
                "Dedicated in respectful memory of Dr. Kasakurthi "
                "Jagadeesh Babu, a neurosurgeon whose life and service "
                "to medicine are remembered with respect."
            )
        }

        # ============================================================
        # NEUROSURGICAL ANATOMY
        # ============================================================

        self.neurosurgical_anatomy = {

            "SCALP": {

                "Meaning": (
                    "S - Skin\n"
                    "C - Connective Tissue\n"
                    "A - Aponeurosis (Galea Aponeurotica)\n"
                    "L - Loose Areolar Connective Tissue\n"
                    "P - Pericranium"
                ),

                "Layers": [

                    {
                        "Layer": 1,
                        "Name": "Skin",
                        "Description": (
                            "The outermost layer containing hair follicles, "
                            "sweat glands and sebaceous glands."
                        )
                    },

                    {
                        "Layer": 2,
                        "Name": "Connective Tissue",
                        "Description": (
                            "Dense connective tissue containing blood vessels, "
                            "nerves and fibrous tissue."
                        )
                    },

                    {
                        "Layer": 3,
                        "Name": "Aponeurosis",
                        "Alternative Name": "Galea Aponeurotica",
                        "Description": (
                            "A tough fibrous sheet associated with the "
                            "occipitofrontalis muscle."
                        )
                    },

                    {
                        "Layer": 4,
                        "Name": "Loose Areolar Connective Tissue",
                        "Description": (
                            "A relatively loose plane allowing movement "
                            "between the superficial scalp and pericranium."
                        )
                    },

                    {
                        "Layer": 5,
                        "Name": "Pericranium",
                        "Description": (
                            "The periosteal covering of the external surface "
                            "of the skull bones."
                        )
                    }
                ],

                "Clinical_Relevance": (
                    "The scalp is clinically important because surgical "
                    "approaches to the skull pass through its anatomical layers."
                )
            },

            "CRANIAL_SURGICAL_SEQUENCE": [
                "SCALP",
                "Pericranium",
                "Skull / Calvaria",
                "Dura Mater",
                "Arachnoid Mater",
                "Subarachnoid Space",
                "Pia Mater",
                "Brain"
            ]
        }

        # ============================================================
        # 22 SKULL BONES
        # ============================================================

        self.skull_database = {

            "Cranial Bones (Neurocranium) - 8": {

                "Frontal Bone": {
                    "Quantity": 1,
                    "Location": "Forehead and anterior cranial region",
                    "Description": (
                        "Forms the forehead, roofs of the orbits and "
                        "part of the anterior cranial fossa."
                    )
                },

                "Parietal Bones": {
                    "Quantity": 2,
                    "Location": "Superior and lateral skull",
                    "Description": (
                        "Paired bones forming much of the roof and "
                        "sides of the cranial vault."
                    )
                },

                "Temporal Bones": {
                    "Quantity": 2,
                    "Location": "Inferolateral skull",
                    "Description": (
                        "Form parts of the lateral skull and cranial base "
                        "and contain structures of the middle and inner ear."
                    )
                },

                "Occipital Bone": {
                    "Quantity": 1,
                    "Location": "Posterior skull and cranial base",
                    "Description": (
                        "Forms the posterior cranial wall and part of the "
                        "cranial base. Contains the foramen magnum."
                    )
                },

                "Sphenoid Bone": {
                    "Quantity": 1,
                    "Location": "Central cranial base",
                    "Description": (
                        "A complex central bone of the cranial base. "
                        "Contains the sella turcica and contributes to "
                        "the middle cranial fossa and orbital structures."
                    )
                },

                "Ethmoid Bone": {
                    "Quantity": 1,
                    "Location": "Between the orbits and nasal cavity",
                    "Description": (
                        "Contributes to the nasal septum, medial orbital "
                        "walls and anterior cranial floor."
                    )
                }
            },

            "Facial Bones (Viscerocranium) - 14": {

                "Maxillae": {
                    "Quantity": 2,
                    "Location": "Upper jaw and midface",
                    "Description": (
                        "Paired bones forming the upper jaw and contributing "
                        "to the hard palate, orbit and nasal cavity."
                    )
                },

                "Palatine Bones": {
                    "Quantity": 2,
                    "Location": "Posterior hard palate",
                    "Description": (
                        "L-shaped paired bones forming the posterior "
                        "part of the hard palate."
                    )
                },

                "Zygomatic Bones": {
                    "Quantity": 2,
                    "Location": "Cheek region",
                    "Description": (
                        "Form the prominence of the cheeks and contribute "
                        "to the lateral orbital walls and zygomatic arches."
                    )
                },

                "Lacrimal Bones": {
                    "Quantity": 2,
                    "Location": "Medial walls of the orbits",
                    "Description": (
                        "Small facial bones associated with the lacrimal "
                        "apparatus and medial orbital wall."
                    )
                },

                "Nasal Bones": {
                    "Quantity": 2,
                    "Location": "Bridge of the nose",
                    "Description": (
                        "Paired bones forming the bony bridge of the nose."
                    )
                },

                "Vomer": {
                    "Quantity": 1,
                    "Location": "Posteroinferior nasal septum",
                    "Description": (
                        "Plowshare-shaped bone forming part of the nasal septum."
                    )
                },

                "Inferior Nasal Conchae": {
                    "Quantity": 2,
                    "Location": "Lateral nasal cavity",
                    "Description": (
                        "Independent facial bones projecting from the "
                        "lateral walls of the nasal cavity."
                    )
                },

                "Mandible": {
                    "Quantity": 1,
                    "Location": "Lower jaw",
                    "Description": (
                        "The largest facial bone and the principal "
                        "movable bone of the skull."
                    )
                }
            }
        }

        # ============================================================
        # SKULL VIEWS
        # ============================================================

        self.skull_views = {

            "Superior View": {
                "Also Called": "Norma Verticalis",
                "Description": "View of the skull from above.",
                "Important_Bones": [
                    "Frontal bone",
                    "Parietal bones",
                    "Occipital bone"
                ],
                "Important_Features": [
                    "Coronal suture",
                    "Sagittal suture",
                    "Lambdoid suture",
                    "Bregma",
                    "Lambda"
                ]
            },

            "Anterior View": {
                "Also Called": "Norma Frontalis",
                "Description": "View of the skull from the front.",
                "Important_Bones": [
                    "Frontal bone",
                    "Nasal bones",
                    "Maxillae",
                    "Zygomatic bones",
                    "Mandible",
                    "Lacrimal bones"
                ],
                "Important_Features": [
                    "Orbits",
                    "Nasal aperture",
                    "Infraorbital foramina",
                    "Supraorbital margins",
                    "Anterior nasal spine"
                ]
            },

            "Posterior View": {
                "Also Called": "Norma Occipitalis",
                "Description": "View of the skull from behind.",
                "Important_Bones": [
                    "Occipital bone",
                    "Parietal bones",
                    "Temporal bones"
                ],
                "Important_Features": [
                    "Lambdoid suture",
                    "External occipital protuberance",
                    "Superior nuchal lines",
                    "Inferior nuchal lines"
                ]
            },

            "Lateral View": {
                "Also Called": "Norma Lateralis",
                "Description": "Side view of the skull.",
                "Important_Bones": [
                    "Frontal bone",
                    "Parietal bone",
                    "Temporal bone",
                    "Occipital bone",
                    "Sphenoid bone",
                    "Zygomatic bone",
                    "Maxilla",
                    "Mandible"
                ],
                "Important_Features": [
                    "Pterion",
                    "Asterion",
                    "Zygomatic arch",
                    "External acoustic meatus",
                    "Mastoid process",
                    "Styloid process",
                    "Mandibular fossa"
                ]
            },

            "Inferior View": {
                "Also Called": "Norma Basalis",
                "Description": "View of the external base of the skull from below.",
                "Important_Bones": [
                    "Occipital bone",
                    "Temporal bones",
                    "Sphenoid bone",
                    "Palatine bones",
                    "Maxillae",
                    "Vomer"
                ],
                "Important_Features": [
                    "Foramen magnum",
                    "Occipital condyles",
                    "Jugular foramina",
                    "Carotid canals",
                    "Foramen ovale",
                    "Foramen spinosum",
                    "Hard palate",
                    "Choanae"
                ]
            },

            "Basal Cranial View": {
                "Also Called": "Norma Basalis",
                "Description": "External inferior view emphasizing the cranial base.",
                "Important_Features": [
                    "Foramen magnum",
                    "Occipital condyles",
                    "Jugular foramen",
                    "Carotid canal",
                    "Foramen lacerum",
                    "Foramen ovale",
                    "Foramen spinosum",
                    "Stylomastoid foramen"
                ]
            }
        }

        # ============================================================
        # SKULL NORMAE
        # ============================================================

        self.skull_normae = {

            "Norma Verticalis": {
                "Meaning": "Superior view",
                "Main_Bones": [
                    "Frontal",
                    "Parietal",
                    "Occipital"
                ],
                "Key_Sutures": [
                    "Coronal",
                    "Sagittal",
                    "Lambdoid"
                ]
            },

            "Norma Frontalis": {
                "Meaning": "Anterior view",
                "Main_Bones": [
                    "Frontal",
                    "Nasal",
                    "Maxilla",
                    "Zygomatic",
                    "Mandible"
                ]
            },

            "Norma Occipitalis": {
                "Meaning": "Posterior view",
                "Main_Bones": [
                    "Occipital",
                    "Parietal",
                    "Temporal"
                ]
            },

            "Norma Lateralis": {
                "Meaning": "Lateral view",
                "Main_Bones": [
                    "Frontal",
                    "Parietal",
                    "Temporal",
                    "Occipital",
                    "Sphenoid",
                    "Zygomatic",
                    "Maxilla",
                    "Mandible"
                ]
            },

            "Norma Basalis": {
                "Meaning": "Inferior / basal view",
                "Main_Bones": [
                    "Occipital",
                    "Temporal",
                    "Sphenoid",
                    "Maxilla",
                    "Palatine",
                    "Vomer"
                ]
            }
        }

        # ============================================================
        # SUTURES
        # ============================================================

        self.sutures = {

            "Coronal Suture":
                "Between frontal and parietal bones.",

            "Sagittal Suture":
                "Between the two parietal bones.",

            "Lambdoid Suture":
                "Between occipital and parietal bones.",

            "Squamous Suture":
                "Between temporal and parietal bones.",

            "Metopic Suture":
                "Midline frontal suture during development; "
                "usually fuses during childhood."
        }

        # ============================================================
        # SKULL LANDMARKS
        # ============================================================

        self.skull_landmarks = {

            "Bregma":
                "Junction of coronal and sagittal sutures.",

            "Lambda":
                "Junction of sagittal and lambdoid sutures.",

            "Pterion":
                "Region where frontal, parietal, temporal and "
                "sphenoid bones meet.",

            "Asterion":
                "Region where parietal, temporal and occipital "
                "bones meet.",

            "Nasion":
                "Midline junction between frontal and nasal bones.",

            "Inion":
                "External occipital protuberance."
        }

        # ============================================================
        # CRANIAL FORAMINA
        # ============================================================

        self.cranial_foramina = {

            "Foramen Magnum":
                "Passage between cranial cavity and vertebral canal.",

            "Optic Canal":
                "Transmits the optic nerve and ophthalmic artery.",

            "Superior Orbital Fissure":
                "Transmits structures including CN III, IV, V1 and VI.",

            "Foramen Rotundum":
                "Transmits the maxillary division of trigeminal nerve (V2).",

            "Foramen Ovale":
                "Transmits the mandibular division of trigeminal nerve (V3).",

            "Foramen Spinosum":
                "Transmits the middle meningeal artery and meningeal branch of V3.",

            "Internal Acoustic Meatus":
                "Transmits facial and vestibulocochlear nerves.",

            "Jugular Foramen":
                "Associated with cranial nerves IX, X and XI and major venous drainage.",

            "Hypoglossal Canal":
                "Transmits the hypoglossal nerve (CN XII).",

            "Carotid Canal":
                "Passage for the internal carotid artery and sympathetic plexus."
        }

    # ================================================================
    # 1-SECOND DELAY FUNCTION
    # ================================================================

    def line_print(self, text=""):
        print(text)
        time.sleep(1)

    # ================================================================
    # MEMORIAL DISPLAY
    # ================================================================

    def display_memorial(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                    MEMORIAL")
        self.line_print("=" * 70)

        self.line_print(
            "\nName        : " + self.memorial["Name"]
        )

        self.line_print(
            "Profession  : " + self.memorial["Profession"]
        )

        self.line_print(
            "Associated  : " + self.memorial["Associated With"]
        )

        self.line_print(
            "Date        : " + self.memorial["Date"]
        )

        self.line_print("\nTribute:")
        self.line_print(self.memorial["Tribute"])

    # ================================================================
    # SCALP DISPLAY
    # ================================================================

    def display_scalp(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                    SCALP")
        self.line_print("=" * 70)

        self.line_print("\nSCALP means:")
        self.line_print(
            self.neurosurgical_anatomy["SCALP"]["Meaning"]
        )

        self.line_print("\nFive anatomical layers:")

        for layer in self.neurosurgical_anatomy["SCALP"]["Layers"]:

            self.line_print(
                f"{layer['Layer']}. {layer['Name']}"
            )

            if "Alternative Name" in layer:
                self.line_print(
                    "   Alternative Name: "
                    + layer["Alternative Name"]
                )

            self.line_print(
                "   Description: "
                + layer["Description"]
            )

    # ================================================================
    # CRANIAL ANATOMICAL SEQUENCE
    # ================================================================

    def display_surgical_sequence(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("              CRANIAL ANATOMICAL PLANES")
        self.line_print("=" * 70)

        sequence = (
            self.neurosurgical_anatomy
            ["CRANIAL_SURGICAL_SEQUENCE"]
        )

        for number, structure in enumerate(sequence, start=1):

            self.line_print(
                f"{number}. {structure}"
            )

        self.line_print(
            "\nEducational anatomy sequence only."
        )

    # ================================================================
    # 22 SKULL BONES
    # ================================================================

    def display_all_bones(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                 22 SKULL BONES")
        self.line_print("=" * 70)

        total = 0

        for category, bones in self.skull_database.items():

            self.line_print("\n" + category)
            self.line_print("-" * 60)

            for bone, details in bones.items():

                self.line_print("\n" + bone)

                self.line_print(
                    "  Quantity   : "
                    + str(details["Quantity"])
                )

                self.line_print(
                    "  Location   : "
                    + details["Location"]
                )

                self.line_print(
                    "  Description: "
                    + details["Description"]
                )

                total += details["Quantity"]

        self.line_print("\n" + "-" * 60)
        self.line_print(
            "TOTAL INDIVIDUAL SKULL BONES: "
            + str(total)
        )

    # ================================================================
    # SKULL VIEWS
    # ================================================================

    def display_skull_views(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                    SKULL VIEWS")
        self.line_print("=" * 70)

        for view, details in self.skull_views.items():

            self.line_print("\n" + view)
            self.line_print("-" * 50)

            self.line_print(
                "Also Called: " + details["Also Called"]
            )

            self.line_print(
                "Description: " + details["Description"]
            )

            self.line_print("Important Bones:")

            if "Important_Bones" in details:

                for bone in details["Important_Bones"]:
                    self.line_print("  - " + bone)

            self.line_print("Important Features:")

            for feature in details["Important_Features"]:
                self.line_print("  - " + feature)

    # ================================================================
    # NORMAE
    # ================================================================

    def display_normae(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                 SKULL NORMAE")
        self.line_print("=" * 70)

        for norma, details in self.skull_normae.items():

            self.line_print("\n" + norma)
            self.line_print("-" * 50)

            self.line_print(
                "Meaning: " + details["Meaning"]
            )

            self.line_print("Main Bones:")

            for bone in details["Main_Bones"]:
                self.line_print("  - " + bone)

            if "Key_Sutures" in details:

                self.line_print("Key Sutures:")

                for suture in details["Key_Sutures"]:
                    self.line_print("  - " + suture)

    # ================================================================
    # SUTURES
    # ================================================================

    def display_sutures(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                  CRANIAL SUTURES")
        self.line_print("=" * 70)

        for suture, description in self.sutures.items():

            self.line_print("\n" + suture)
            self.line_print("  " + description)

    # ================================================================
    # LANDMARKS
    # ================================================================

    def display_landmarks(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                  SKULL LANDMARKS")
        self.line_print("=" * 70)

        for landmark, description in self.skull_landmarks.items():

            self.line_print("\n" + landmark)
            self.line_print("  " + description)

    # ================================================================
    # FORAMINA
    # ================================================================

    def display_foramina(self):

        self.line_print("\n" + "=" * 70)
        self.line_print("                 CRANIAL FORAMINA")
        self.line_print("=" * 70)

        for foramen, description in self.cranial_foramina.items():

            self.line_print("\n" + foramen)
            self.line_print("  " + description)

    # ================================================================
    # BRAIN SURGERY EDUCATIONAL SIMULATION
    # ================================================================

    def display_brain_surgery_simulation(self):

        self.line_print("\n\n" + "=" * 70)
        self.line_print("              BRAIN SURGERY SIMULATION")
        self.line_print("=" * 70)

        self.line_print("\nSurgeon:")
        self.line_print("Dr. Kasakurthi Jagadeesh")

        self.line_print("\nProcedure:")
        self.line_print("Educational Brain Surgery Simulation")

        self.line_print("\nPatient:")
        self.line_print("Simulated Patient")

        # ------------------------------------------------------------
        # PREOPERATIVE PHASE
        # ------------------------------------------------------------

        self.line_print("\n" + "-" * 70)
        self.line_print("                    PREOPERATIVE PHASE")
        self.line_print("-" * 70)

        self.line_print("\nPatient preparation begins.")

        self.line_print(
            "Anesthesia is administered by the anesthesia team."
        )

        self.line_print(
            "The simulated patient is continuously monitored."
        )

        # ------------------------------------------------------------
        # SCALP
        # ------------------------------------------------------------

        self.line_print("\n" + "-" * 70)
        self.line_print("                    SCALP ANATOMY")
        self.line_print("-" * 70)

        self.line_print(
            "\nDr. Kasakurthi Jagadeesh identifies the five "
            "anatomical layers of the SCALP:"
        )

        scalp_layers = [
            "1. Skin",
            "2. Dense Connective Tissue",
            "3. Aponeurosis (Galea Aponeurotica)",
            "4. Loose Areolar Connective Tissue",
            "5. Pericranium"
        ]

        for layer in scalp_layers:
            self.line_print(layer)

        # ------------------------------------------------------------
        # CRANIAL FIELD
        # ------------------------------------------------------------

        self.line_print("\n" + "-" * 70)
        self.line_print("                  CRANIAL ANATOMY")
        self.line_print("-" * 70)

        self.line_print(
            "\nThe simulation reaches the cranial surgical field."
        )

        self.line_print(
            "The skull / calvaria is identified."
        )

        self.line_print(
            "The meninges and brain are recognized as deeper "
            "anatomical structures."
        )

        # ------------------------------------------------------------
        # EDUCATIONAL NOTICE
        # ------------------------------------------------------------

        self.line_print("\n" + "-" * 70)
        self.line_print("                 EDUCATIONAL NOTICE")
        self.line_print("-" * 70)

        self.line_print(
            "\nThis is a fictional educational simulation "
            "for studying anatomy."
        )

        self.line_print(
            "It does not provide instructions for performing "
            "brain surgery on a real patient."
        )

        # ------------------------------------------------------------
        # FINAL LINE
        # ------------------------------------------------------------

        self.line_print("\n" + "=" * 70)
        self.line_print("              END OF SIMULATION")
        self.line_print("=" * 70)

        self.line_print(
            "\n Manideepak Kumar Batchu"
        )

    # ================================================================
    # MAIN RUNNER
    # ================================================================

    def run(self):

        self.display_memorial()

        self.display_scalp()

        self.display_surgical_sequence()

        self.display_all_bones()

        self.display_skull_views()

        self.display_normae()

        self.display_sutures()

        self.display_landmarks()

        self.display_foramina()

        # Final simulation
        self.display_brain_surgery_simulation()


# ====================================================================
# PROGRAM START
# ====================================================================

if __name__ == "__main__":

    explorer = SkullOsteologyExplorer()

    explorer.run()