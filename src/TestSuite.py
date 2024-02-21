import os
import sys
sys.path.append(os.path.dirname(__file__))
import ColorFormat

class TestSuite:
    def __init__(self, suiteName: str):
        """
        Constructor
        """

        self.suiteName: str = suiteName
        self.tests: list[tuple[str, callable]] = []
        self.setup: callable = lambda: True
        self.before: callable = lambda: True


    def addTest(self, testName: str, test: callable):
        """
        Add a test to the suite
        """

        self.tests.append((testName, test))


    def setSetup(self, setup: callable):
        """
        Set the setup function
        """

        self.setup = setup


    def setBefore(self, before: callable):
        """
        Set the before function
        """

        self.before = before


    def runTests(self):
        """
        Run all the tests in the suite
        """

        print(
                ColorFormat.ColorFormatBuilder.begin()
                .setFormat(ColorFormat.STYLE.BOLD)
                .setFormat(ColorFormat.STYLE.UNDERLINE)
                .addText(f"Test Suite: {self.suiteName}")
                .build()
                )

        if len(self.tests) == 0:
            print(
                    ColorFormat.ColorFormatBuilder.begin()
                    .setFormat(ColorFormat.STYLE.ITALIC)
                    .setFormat(ColorFormat.STYLE.UNDERLINE)
                    .addText("No tests to run")
                    .build()
                    )

            return

        if not self.setup():
            print(
                    ColorFormat.ColorFormatBuilder.begin()
                    .setFormat(
                        ColorFormat.STYLE.BOLD, ColorFormat.COLOR.RED
                        )
                    .addText("Setup function failed")
                    .resetFormat()
                    .addText(" - ")
                    .setFormat(ColorFormat.STYLE.ITALIC)
                    .setFormat(
                        ColorFormat.STYLE.UNDERLINE, ColorFormat.COLOR.YELLOW
                        )
                    .addText("ALL TESTS SKIPPED")
                    .build()
                    )

            return

        passed_tests: list[str] = []
        failed_tests: list[str] = []
        for (test_name, test) in self.tests:

            if not self.before():
                print(
                        ColorFormat.ColorFormatBuilder.begin()
                        .setFormat(ColorFormat.STYLE.BOLD, ColorFormat.COLOR.RED)
                        .addText("Before function failed")
                        .resetFormat()
                        .addText(f" - Test: {test_name} ... ")
                        .setFormat(ColorFormat.STYLE.ITALIC)
                        .setFormat(
                            ColorFormat.STYLE.UNDERLINE, ColorFormat.COLOR.YELLOW
                            )
                        .addText("SKIPPED")
                        .build()
                        )

                continue

            if test():
                print(
                        ColorFormat.ColorFormatBuilder.begin()
                        .addText(f"Test: {test_name} ... ")
                        .setFormat(ColorFormat.STYLE.ITALIC)
                        .setFormat(
                            ColorFormat.STYLE.UNDERLINE, ColorFormat.COLOR.GREEN
                            )
                        .addText("PASSED")
                        .build()
                        )

                passed_tests.append(test_name)
            else:
                print(
                        ColorFormat.ColorFormatBuilder.begin()
                        .addText(f"Test: {test_name} ... ")
                        .setFormat(ColorFormat.STYLE.ITALIC)
                        .setFormat(
                            ColorFormat.STYLE.UNDERLINE, ColorFormat.COLOR.RED
                            )
                        .addText("FAILED")
                        .build()
                        )

                failed_tests.append(test_name)

        print(
                ColorFormat.ColorFormatBuilder.begin()
                .setFormat(ColorFormat.STYLE.BOLD)
                .setFormat(ColorFormat.STYLE.UNDERLINE)
                .addText("\nSummary:")
                .setFormat(
                    ColorFormat.STYLE.ITALIC, ColorFormat.COLOR.GREEN
                    )
                .addText(
                    f"\nPassed Tests: {len(passed_tests)/len(self.tests)*100:.2f}%\n"
                    )
                .addText("\n".join([f"- {test}" for test in passed_tests]))
                .setFormat(
                    ColorFormat.STYLE.ITALIC, ColorFormat.COLOR.RED
                    )
                .addText(f"\nFailed Tests:\n")
                .addText("\n".join([f"- {test}" for test in failed_tests]))
                )
