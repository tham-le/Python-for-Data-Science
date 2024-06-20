import sys
import os


def ft_tqdm(lst: range) -> None:
    """
        Decorate an iterable object, returning an iterator \
which acts exactly like the original iterable, but prints a \
dynamically updating progressbar every time a value is requested.\n
"""
    total = len(lst)
    length = os.get_terminal_size().columns * 3 // 5
    i = 1
    for item in lst:
        p = i / total
        progess = "█" * int(p * length)
        sys.stdout.write("\r" + f"{p:4.0%} |{progess.ljust(length)}| \
{i}/{total}")
        sys.stdout.flush()
        yield item
        i += 1
