// https://adventofcode.com/2022/day/1
import scala.io.Source

var caloriesByElves: Vector[Int] = Vector()
var calories = 0

@main def main() = {
  for (line <- Source.fromFile("input.txt").getLines) {
    if (line == "") {
      caloriesByElves = caloriesByElves :+ calories
      calories = 0
    } else {
      calories += line.toInt
    }
  }

  // part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
  println(caloriesByElves.max)

  // part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
  println(caloriesByElves.sortWith(_ > _).slice(0, 3).sum)
}