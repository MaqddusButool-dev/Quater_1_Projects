def hangman_stages(attempts):
    stages = [
        """
         _______
         |     |
         |     O
         |    /|\\
         |    / \\
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|\\
         |    /
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|\\
         |
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |    /|
         |
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |     |
         |
         |
        _|_
        """,
        """
         _______
         |     |
         |     O
         |
         |
         |
        _|_
        """,
        """
         _______
         |     |
         |
         |
         |
         |
        _|_
        """
    ]
    return stages[attempts]
