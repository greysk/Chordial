# Chordial
Chord Progression Suggester

## Note on changes in this branch

See [changelog.md](/changelog.md) and the linked commits inside for details.

You can ignore the second commit which is most of the adjustments made to match the code format to [PEP8](https://www.python.org/dev/peps/pep-0008/) which does not affect how the code runs.

The major/most import changes done are in these commits:
1. [Remove unneeded imports](https://github.com/greysk/Chordial/commit/6d8c0e0da774dba490ba06a408af67ac45bd998c)
2. [Remove extraneous code](https://github.com/greysk/Chordial/commit/798e79753a05cc5b458c6fda1739907aa7e7ec7f)
3. [Change `self.mysound` to `mysound` & Add `self.file_to_open = None` to `ProgramBody.__init__()`](https://github.com/greysk/Chordial/commit/0c23d11630f2cf0caa29c6a60c741ce00365271b) (In preparation for commit below.)
4. [Move `def __init__()` to the top of `class ProgramBody`](https://github.com/greysk/Chordial/commit/4bf933fcaa9258fda084f4c13bb7aa69db9b73eb)
    - See Python Documentation Tutorial on [Class Objects](https://docs.python.org/3/tutorial/classes.html#class-objects) and [Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables) for more information

