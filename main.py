import random

# Representasi individu dalam populasi
class Schedule:
    def __init__(self, labs):
        self.labs = labs
        self.fitness = 0

    def generate(self):
        # Mengacak urutan penjadwalan praktikum
        random.shuffle(self.labs)

    def calculate_fitness(self):
        # Menghitung nilai fitness berdasarkan aturan tertentu
        # Misalnya, menghindari tumpang tindih waktu praktikum di lab yang sama
        # dan mencoba menyebarkan praktikum dengan baik di sepanjang minggu

        # Implementasikan aturan penilaian yang sesuai dengan kebutuhan Anda
        pass

# Operasi seleksi menggunakan turnamen
def selection(population):
    tournament_size = 5
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        best = min(tournament, key=lambda x: x.fitness)
        selected.append(best)
    return selected

# Operasi reproduksi menggunakan crossover satu titik
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.labs) - 1)
    child1 = Schedule(parent1.labs[:crossover_point] + parent2.labs[crossover_point:])
    child2 = Schedule(parent2.labs[:crossover_point] + parent1.labs[crossover_point:])
    return child1, child2

# Operasi mutasi dengan menukar dua praktikum
def mutation(individual):
    mutation_point1 = random.randint(0, len(individual.labs) - 1)
    mutation_point2 = random.randint(0, len(individual.labs) - 1)
    individual.labs[mutation_point1], individual.labs[mutation_point2] = individual.labs[mutation_point2], individual.labs[mutation_point1]

def genetic_algorithm(lab_list, population_size, generations):
    population = []
    for _ in range(population_size):
        schedule = Schedule(lab_list)
        schedule.generate()
        population.append(schedule)

    for _ in range(generations):
        for individual in population:
            individual.calculate_fitness()

        population = sorted(population, key=lambda x: x.fitness)

        selected = selection(population)

        new_population = []

        for i in range(0, len(selected), 2):
            parent1 = selected[i]
            parent2 = selected[i + 1]

            child1, child2 = crossover(parent1, parent2)

            mutation(child1)
            mutation(child2)

            new_population.extend([child1, child2])

        population = new_population

    best_schedule = population[0]
    return best_schedule

# Contoh penggunaan
lab_list = ["Lab A", "Lab B", "Lab C"]  # Daftar lab (bisa diubah)
population_size = 100
generations = 1

best_schedule = genetic_algorithm(lab_list, population_size, generations)

print("Jadwal Terbaik:")
for index, lab in enumerate(best_schedule.labs):
    print("Praktikum", index+1, "di", lab)