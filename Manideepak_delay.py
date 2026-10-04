import time


class SkullOsteologyExplorer:

    # ============================================================
    # DELAY CONFIGURATION
    # ============================================================

    MAIN_DELAY = 0.50
    LINE_DELAY = 0.30

    # Set False if you want to disable all delays
    ENABLE_DELAY = True

    def __init__(self):

        # ========================================================
        # MEMORIAL
        # ========================================================

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

        # ========================================================
        # NEUROSURGICAL ANATOMY
        # ========================================================

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
                            "between superficial scalp and pericranium."
                        )
                    },

                    {
                        "Layer": 5,
                        "Name": "Pericranium",
                        "Description": (
                            "The periosteal covering of the external surface "
                            "of the skull."
                        )
                    }
                ]
            },

            "CRANIAL_SEQUENCE": [
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

        # ========================================================
        # 22 SKULL BONES
        # ========================================================

        self.skull_database = {

            "CRANIAL BONES — NEUROCRANIUM": {

                "Frontal Bone": {
                    "Quantity": 1,
                    "Location": "Forehead and anterior cranial region",
                    "Description": (
                        "Forms the forehead, orbital roofs and part "
                        "of the anterior cranial fossa."
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
                        "Contribute to the lateral skull and cranial base "
                        "and contain structures associated with hearing "
                        "and balance."
                    )
                },

                "Occipital Bone": {
                    "Quantity": 1,
                    "Location": "Posterior skull and cranial base",
                    "Description": (
                        "Forms the posterior cranial wall and contains "
                        "the foramen magnum."
                    )
                },

                "Sphenoid Bone": {
                    "Quantity": 1,
                    "Location": "Central cranial base",
                    "Description": (
                        "Complex central bone contributing to the cranial "
                        "base, orbit and middle cranial fossa."
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

            "FACIAL BONES — VISCEROCRANIUM": {

                "Maxillae": {
                    "Quantity": 2,
                    "Location": "Upper jaw and midface",
                    "Description": (
                        "Form the upper jaw and contribute to the orbit, "
                        "nasal cavity and hard palate."
                    )
                },

                "Palatine Bones": {
                    "Quantity": 2,
                    "Location": "Posterior hard palate",
                    "Description": (
                        "Paired bones contributing to the posterior "
                        "hard palate."
                    )
                },

                "Zygomatic Bones": {
                    "Quantity": 2,
                    "Location": "Cheek region",
                    "Description": (
                        "Form the cheek prominence and contribute to "
                        "the orbit and zygomatic arches."
                    )
                },

                "Lacrimal Bones": {
                    "Quantity": 2,
                    "Location": "Medial orbital walls",
                    "Description": (
                        "Small bones contributing to the medial "
                        "orbital walls."
                    )
                },

                "Nasal Bones": {
                    "Quantity": 2,
                    "Location": "Bridge of nose",
                    "Description": (
                        "Paired bones forming the bony bridge of the nose."
                    )
                },

                "Vomer": {
                    "Quantity": 1,
                    "Location": "Nasal septum",
                    "Description": (
                        "Forms part of the inferior nasal septum."
                    )
                },

                "Inferior Nasal Conchae": {
                    "Quantity": 2,
                    "Location": "Lateral nasal cavity",
                    "Description": (
                        "Independent bones projecting from the lateral "
                        "walls of the nasal cavity."
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

        # ========================================================
        # SKULL VIEWS
        # ========================================================

        self.skull_views = {

            "SUPERIOR VIEW — NORMA VERTICALIS": [
                "Frontal bone",
                "Parietal bones",
                "Occipital bone",
                "Coronal suture",
                "Sagittal suture",
                "Lambdoid suture",
                "Bregma",
                "Lambda"
            ],

            "ANTERIOR VIEW — NORMA FRONTALIS": [
                "Frontal bone",
                "Nasal bones",
                "Maxillae",
                "Zygomatic bones",
                "Mandible",
                "Orbits",
                "Nasal aperture",
                "Supraorbital margins",
                "Anterior nasal spine"
            ],

            "POSTERIOR VIEW — NORMA OCCIPITALIS": [
                "Occipital bone",
                "Parietal bones",
                "Temporal bones",
                "Lambdoid suture",
                "External occipital protuberance",
                "Superior nuchal lines",
                "Inferior nuchal lines"
            ],

            "LATERAL VIEW — NORMA LATERALIS": [
                "Frontal bone",
                "Parietal bone",
                "Temporal bone",
                "Occipital bone",
                "Sphenoid bone",
                "Zygomatic bone",
                "Maxilla",
                "Mandible",
                "Pterion",
                "Asterion",
                "Zygomatic arch",
                "External acoustic meatus",
                "Mastoid process",
                "Styloid process"
            ],

            "INFERIOR VIEW — NORMA BASALIS": [
                "Occipital bone",
                "Temporal bones",
                "Sphenoid bone",
                "Palatine bones",
                "Maxillae",
                "Vomer",
                "Foramen magnum",
                "Occipital condyles",
                "Jugular foramina",
                "Carotid canals",
                "Foramen ovale",
                "Foramen spinosum",
                "Hard palate",
                "Choanae"
            ]
        }

        # ========================================================
        # SUTURES
        # ========================================================

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
                "Midline frontal suture during development."
        }

        # ========================================================
        # LANDMARKS
        # ========================================================

        self.landmarks = {

            "Bregma":
                "Junction of coronal and sagittal sutures.",

            "Lambda":
                "Junction of sagittal and lambdoid sutures.",

            "Pterion":
                "Meeting region of frontal, parietal, temporal "
                "and sphenoid bones.",

            "Asterion":
                "Meeting region of parietal, temporal and occipital bones.",

            "Nasion":
                "Midline junction of frontal and nasal bones.",

            "Inion":
                "External occipital protuberance.",

            "Glabella":
                "Smooth prominence of the frontal bone."
        }

        # ========================================================
        # CRANIAL FORAMINA
        # ========================================================

        self.foramina = {

            "Foramen Magnum":
                "Major opening between cranial cavity and vertebral canal.",

            "Optic Canal":
                "Transmits optic nerve and ophthalmic artery.",

            "Superior Orbital Fissure":
                "Associated with cranial nerves III, IV, V1 and VI.",

            "Foramen Rotundum":
                "Transmits maxillary division of trigeminal nerve V2.",

            "Foramen Ovale":
                "Transmits mandibular division of trigeminal nerve V3.",

            "Foramen Spinosum":
                "Associated with the middle meningeal artery.",

            "Internal Acoustic Meatus":
                "Transmits facial and vestibulocochlear nerves.",

            "Jugular Foramen":
                "Associated with cranial nerves IX, X and XI.",

            "Hypoglossal Canal":
                "Transmits hypoglossal nerve CN XII.",

            "Carotid Canal":
                "Passage for the internal carotid artery."
        }

    # ============================================================
    # OUTPUT FUNCTIONS
    # ============================================================

    def main_line(self, text=""):

        print(text)

        if self.ENABLE_DELAY:
            time.sleep(self.MAIN_DELAY)

    def line(self, text=""):

        print(text)

        if self.ENABLE_DELAY:
            time.sleep(self.LINE_DELAY)

    # ============================================================
    # SECTION HEADER
    # ============================================================

    def section(self, title):

        self.main_line("")
        self.main_line("=" * 70)
        self.main_line(title.center(70))
        self.main_line("=" * 70)

    # ============================================================
    # MEMORIAL
    # ============================================================

    def display_memorial(self):

        self.section("MEMORIAL")

        self.line(
            "Name       : " + self.memorial["Name"]
        )

        self.line(
            "Profession : " + self.memorial["Profession"]
        )

        self.line(
            "Associated : " + self.memorial["Associated With"]
        )

        self.line(
            "Date       : " + self.memorial["Date"]
        )

        self.main_line("")
        self.main_line("TRIBUTE")

        self.line(
            self.memorial["Tribute"]
        )

    # ============================================================
    # SCALP
    # ============================================================

    def display_scalp(self):

        self.section("SCALP — FIVE LAYERS")

        self.main_line("SCALP MEANING")

        self.line("S — Skin")
        self.line("C — Connective Tissue")
        self.line("A — Aponeurosis / Galea Aponeurotica")
        self.line("L — Loose Areolar Connective Tissue")
        self.line("P — Pericranium")

        self.main_line("")
        self.main_line("ANATOMICAL LAYERS")

        for layer in self.neurosurgical_anatomy["SCALP"]["Layers"]:

            self.main_line(
                f"{layer['Layer']}. {layer['Name']}"
            )

            if "Alternative Name" in layer:

                self.line(
                    "Alternative Name: "
                    + layer["Alternative Name"]
                )

            self.line(
                "Description: "
                + layer["Description"]
            )

    # ============================================================
    # CRANIAL ANATOMICAL SEQUENCE
    # ============================================================

    def display_sequence(self):

        self.section("CRANIAL ANATOMICAL PLANES")

        sequence = (
            self.neurosurgical_anatomy
            ["CRANIAL_SEQUENCE"]
        )

        for number, structure in enumerate(sequence, 1):

            self.main_line(
                f"{number}. {structure}"
            )

        self.line("")
        self.line(
            "Educational anatomy sequence only."
        )

    # ============================================================
    # SKULL BONES
    # ============================================================

    def display_bones(self):

        self.section("22 SKULL BONES")

        total = 0

        for category, bones in self.skull_database.items():

            self.main_line("")
            self.main_line(category)

            self.line("-" * 60)

            for bone, details in bones.items():

                self.main_line(
                    bone
                )

                self.line(
                    "Quantity   : "
                    + str(details["Quantity"])
                )

                self.line(
                    "Location   : "
                    + details["Location"]
                )

                self.line(
                    "Description: "
                    + details["Description"]
                )

                total += details["Quantity"]

        self.main_line("")
        self.main_line(
            "TOTAL INDIVIDUAL SKULL BONES = "
            + str(total)
        )

    # ============================================================
    # SKULL VIEWS
    # ============================================================

    def display_views(self):

        self.section("SKULL VIEWS / NORMAE")

        for view, structures in self.skull_views.items():

            self.main_line("")
            self.main_line(view)

            self.line("-" * 60)

            for structure in structures:

                self.line(
                    "• " + structure
                )

    # ============================================================
    # SUTURES
    # ============================================================

    def display_sutures(self):

        self.section("CRANIAL SUTURES")

        for name, description in self.sutures.items():

            self.main_line(name)

            self.line(
                description
            )

    # ============================================================
    # LANDMARKS
    # ============================================================

    def display_landmarks(self):

        self.section("SKULL LANDMARKS")

        for name, description in self.landmarks.items():

            self.main_line(name)

            self.line(
                description
            )

    # ============================================================
    # FORAMINA
    # ============================================================

    def display_foramina(self):

        self.section("CRANIAL FORAMINA")

        for name, description in self.foramina.items():

            self.main_line(name)

            self.line(
                description
            )

    # ============================================================
    # EDUCATIONAL BRAIN SURGERY SIMULATION
    # ============================================================

    def display_brain_surgery(self):

        self.section("EDUCATIONAL BRAIN SURGERY SIMULATION")

        self.main_line("SURGEON")
        self.line("Dr. Kasakurthi Jagadeesh")

        self.main_line("")
        self.main_line("PATIENT")
        self.line("Simulated Patient")

        self.main_line("")
        self.main_line("PHASE 1 — ANESTHESIA")

        self.line(
            "Anesthesia is represented conceptually."
        )

        self.line(
            "The simulated patient is continuously monitored."
        )

        self.main_line("")
        self.main_line("PHASE 2 — SCALP ANATOMY")

        for layer in self.neurosurgical_anatomy["SCALP"]["Layers"]:

            self.main_line(
                f"Layer {layer['Layer']}: {layer['Name']}"
            )

            self.line(
                layer["Description"]
            )

        self.main_line("")
        self.main_line("PHASE 3 — CRANIAL ANATOMY")

        self.line(
            "The simulation studies the skull / calvaria."
        )

        self.line(
            "The meninges are identified conceptually."
        )

        self.line(
            "The brain is studied as the deeper neurological structure."
        )

        self.main_line("")
        self.main_line("PHASE 4 — MENINGEAL ANATOMY")

        for structure in [
            "Dura Mater",
            "Arachnoid Mater",
            "Subarachnoid Space",
            "Pia Mater"
        ]:

            self.line(
                "• " + structure
            )

        self.main_line("")
        self.main_line("PHASE 5 — BRAIN ANATOMY")

        for structure in [
            "Cerebral Cortex",
            "White Matter",
            "Deep Brain Structures",
            "Ventricular System",
            "Brainstem",
            "Cerebellum"
        ]:

            self.line(
                "• " + structure
            )

        self.main_line("")
        self.main_line("EDUCATIONAL SAFETY NOTICE")

        self.line(
            "This is a fictional educational anatomy simulation."
        )

        self.line(
            "It is not a clinical surgical protocol."
        )

        self.line(
            "Real neurosurgery requires extensive medical education,"
        )

        self.line(
            "supervised clinical training and qualified specialists."
        )

    # ============================================================
    # FINAL
    # ============================================================

    def final_screen(self):

        self.section("END OF SKULL OSTEOLOGY EXPLORER")

        self.main_line(
            "Dedicated to anatomical education and lifelong learning."
        )

        self.main_line("")
        self.main_line(
            "In respectful memory of"
        )

        self.main_line(
            "Dr. Kasakurthi Jagadeesh Babu"
        )

        self.main_line("")

        self.main_line(
            "మణిదీపక్ కుమార్ బచ్చు"
        )

        self.main_line(
            "Manideepak Kumar Batchu"
        )

        self.main_line("")
        self.main_line(
            "PROGRAM COMPLETED"
        )

    # ============================================================
    # MAIN RUNNER
    # ============================================================

    def run(self):

        self.display_memorial()

        self.display_scalp()

        self.display_sequence()

        self.display_bones()

        self.display_views()

        self.display_sutures()

        self.display_landmarks()

        self.display_foramina()

        self.display_brain_surgery()

        self.final_screen()


# ================================================================
# PROGRAM START
# ================================================================

if __name__ == "__main__":

    explorer = SkullOsteologyExplorer()

    explorer.run()