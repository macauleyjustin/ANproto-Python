import unittest

from anproto.an import Gen, Hash, Sign, Open


class TestANProto(unittest.TestCase):
    def test_gen_hash_sign_open(self):
        k = Gen()
        self.assertEqual(len(k), 132)
        h = Hash("hello")
        signed = Sign("hello", k)
        self.assertEqual(signed[:44], k[:44])
        opened = Open(signed)
        self.assertTrue(opened.endswith("hello"))

    def test_readme_examples(self):
        example_hash = "pZGm1Av0IEBKARczz7exkNYsZb8LzaMrV7J32a2fFG4="
        example_signed = (
            "BSY7/er4VJIu08o39NaRAiPY/MAvd7oQhlGCRDABjYU="
            "yVpD8i7d3d4dls3YThEg1x1vSdmqeEweV4e4Ejl/8yPoVG7JR0YAKDPagQOgxXMrlCVLNNqvlNvj4xRDOYDLBjE3NTUxOTc4NDEzMTlwWkdtMUF2MElFQktBUmN6ejdleGtOWXNaYjhMemFNclY3SjMyYTJmRkc0PQ=="
        )
        self.assertEqual(Hash("Hello World"), example_hash)
        opened = Open(example_signed)
        expected_opened = "1755197841319pZGm1Av0IEBKARczz7exkNYsZb8LzaMrV7J32a2fFG4="
        self.assertEqual(opened, expected_opened)


if __name__ == "__main__":
    unittest.main()
