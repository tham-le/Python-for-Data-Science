#!/usr/bin/env python3.10

from load_csv import load
import matplotlib.pyplot as plt


def process_population(population):
    """Convert the population data to floats.
    replace the "M" and "k" suffixes with the correct multiplier
    and convert the strings to floats.
    """
    for i in range(len(population)):
        if population[i].endswith("M"):
            population[i] = float(population[i].replace("M", "")) * 1e6
        elif population[i].endswith("k"):
            population[i] = float(population[i].replace("k", "")) * 1e3
    return population


def million_formatter(x, pos):
    """Format the y-axis labels to millions."""
    return f"{x/1e6:.0f}M"


def main():

    """Plot the population of France and Belgium from 1950 to 2100."""
    try:
        data = load("../population_total.csv")
        if data is None:
            raise Exception("Data is not loaded")
        if len(data) == 0:
            raise Exception("Data is empty")
        if ("country" not in data.columns):
            raise Exception("Data is not in the correct format")
        plt.figure(figsize=(10, 8))
        countries = ["Belgium", "France"]
        countries_name = ""
        max_population = 0
        for country in countries:
            if country not in data["country"].values:
                print(country + " is not in the data")
                continue
            country_data = data[data["country"] == country]
            years = country_data.columns[1:].astype(int)
            population = process_population(country_data.values[0][1:])
            plt.plot(years, population, label=country)
            plt.xticks(years[::40])
            plt.xlim(1800, 2050)
            plt.legend()
            countries_name += country + " "
            if max(population) > max_population:
                max_population = max(population)

        plt.title("Population Projection of " + countries_name)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.gca().yaxis.set_major_locator(plt.MaxNLocator(4))
        plt.gca().yaxis.set_major_formatter(
            plt.FuncFormatter(million_formatter))
        plt.gca().legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
