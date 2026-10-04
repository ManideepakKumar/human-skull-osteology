import sys
import time


class SkullOsteologyExplorer:

    def __init__(self):

        # ============================================================
        # TRIBUTE / MEMORIAL
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
        # SKULL OSTEOLOGY DATABASE
        # 22 INDIVIDUAL BONES
        # ============================================================

        self.skull_database = {

            "Cranial Bones (Neurocranium) - Total: 8": {

                "Frontal Bone": {
                    "Quantity": 1,
                    "Location": "Forehead and superior orbits",
                    "Description": (
                        "Forms the forehead, the roofs of the eye sockets, "
                        "and most of the anterior cranial fossa."
                    )
                },

                "Parietal Bones": {
                    "Quantity": 2,
                    "Location": "Sides and roof of cranium",
                    "Description": (
                        "Form the major portion of the lateral and superior "
                        "walls of the cranial cavity."
                    )
                },

                "Temporal Bones": {
                    "Quantity": 2,
                    "Location": "Sides and base of skull",
                    "Description": (
                        "Form the inferolateral aspects of the skull and parts "
                        "of the cranial floor; house the middle and inner ear structures."
                    )
                },

                "Occipital Bone": {
                    "Quantity": 1,
                    "Location": "Back and base of skull",
                    "Description": (
                        "Forms the back of the skull and base; features the "
                        "foramen magnum through which the spinal cord passes."
                    )
                },

                "Sphenoid Bone": {
                    "Quantity": 1,
                    "Location": "Middle base of skull (Keystone bone)",
                    "Description": (
                        "Spans the width of the cranial floor; features the "
                        "sella turcica which houses and protects the pituitary gland."
                    )
                },

                "Ethmoid Bone": {
                    "Quantity": 1,
                    "Location": "Between nasal cavity and orbits",
                    "Description": (
                        "Complex, lightweight bone forming part of the nasal "
                        "septum, medial orbital walls, and roof of the nasal cavity."
                    )
                }
            },

            "Facial Bones (Viscerocranium) - Total: 14": {

                "Maxillae": {
                    "Quantity": 2,
                    "Location": "Upper jaw and central face",
                    "Description": (
                        "The keystone bones of the face; form the upper jaw, "
                        "hard palate, and inferior eye socket walls."
                    )
                },

                "Palatine Bones": {
                    "Quantity": 2,
                    "Location": "Posterior hard palate",
                    "Description": (
                        "L-shaped bones forming the posterior third of the hard "
                        "palate and parts of the nasal cavity."
                    )
                },

                "Zygomatic Bones": {
                    "Quantity": 2,
                    "Location": "Cheeks",
                    "Description": (
                        "Commonly known as the cheekbones; articulate with the "
                        "temporal bones to form the zygomatic arches."
                    )
                },

                "Lacrimal Bones": {
                    "Quantity": 2,
                    "Location": "Medial eye orbits",
                    "Description": (
                        "The smallest facial bones; contain the lacrimal fossa "
                        "associated with the tear drainage system."
                    )
                },

                "Nasal Bones": {
                    "Quantity": 2,
                    "Location": "Bridge of the nose",
                    "Description": (
                        "Small, rectangular bones forming the bony bridge of the nose."
                    )
                },

                "Vomer": {
                    "Quantity": 1,
                    "Location": "Nasal septum",
                    "Description": (
                        "Slender, plowshare-shaped bone forming the inferior "
                        "and posterior part of the nasal septum."
                    )
                },

                "Inferior Nasal Conchae": {
                    "Quantity": 2,
                    "Location": "Lateral walls of nasal cavity",
                    "Description": (
                        "Scroll-like bones attached to the lateral walls of "
                        "the nasal cavity that help condition inhaled air."
                    )
                },

                "Mandible": {
                    "Quantity": 1,
                    "Location": "Lower jaw",
                    "Description": (
                        "The largest and strongest facial bone and the only "
                        "movable bone of the skull."
                    )
                }
            }
        }


    # ================================================================
    # PRINT WITH 1-SECOND DELAY
    # ================================================================

    def line_print(self, text, delay=1.0):
        """
        Prints one line and waits exactly 1 second.
        """
        print(text)
        time.sleep(delay)


    # ================================================================
    # MEMORIAL
    # ================================================================

    def display_memorial(self):

        self.line_print("")
        self.line_print("=" * 70)
        self.line_print("                     IN MEMORIAM")
        self.line_print("=" * 70)

        self.line_print("")
        self.line_print("             Dr. Kasakurthi Jagadeesh Babu")
        self.line_print("                       Neurosurgeon")
        self.line_print("")
        self.line_print("                  September 2026")
        self.line_print("")
        self.line_print("-" * 70)

        self.line_print(
            "Dedicated in respectful memory of a physician"
        )

        self.line_print(
            "whose service to medicine touched many lives."
        )

        self.line_print("")

        self.line_print(
            "May his memory remain a source of inspiration"
        )

        self.line_print(
            "for those who study medicine and serve humanity."
        )

        self.line_print("")
        self.line_print("                       OM SHANTI")
        self.line_print("=" * 70)
        self.line_print("")


    # ================================================================
    # DISPLAY ALL BONES
    # ================================================================

    def display_all_bones(self):

        self.line_print("=" * 70)
        self.line_print("             HUMAN SKULL OSTEOLOGY DATABASE")
        self.line_print("                           v1.0")
        self.line_print("=" * 70)

        total_bones_count = 0

        for category, bones in self.skull_database.items():

            self.line_print("")
            self.line_print(f"[+] {category.upper()}")
            self.line_print("-" * 70)

            for bone_name, details in bones.items():

                qty = details["Quantity"]
                loc = details["Location"]
                desc = details["Description"]

                total_bones_count += qty

                self.line_print("")
                self.line_print(
                    f" * {bone_name} (Qty: {qty})"
                )

                self.line_print(
                    f"   Location: {loc}"
                )

                self.line_print(
                    f"   -> Function/Detail: {desc}"
                )

        self.line_print("")
        self.line_print("=" * 70)

        self.line_print(
            f"OSTEOLOGY AUDIT COMPLETE: "
            f"{total_bones_count} Total Skull Bones Cataloged."
        )

        self.line_print("=" * 70)


    # ================================================================
    # RUN PROGRAM
    # ================================================================

    def run(self):

        # Display memorial first
        self.display_memorial()

        # Display skull database
        self.display_all_bones()


# ====================================================================
# PROGRAM START
# ====================================================================

if __name__ == "__main__":

    explorer = SkullOsteologyExplorer()
    explorer.run()