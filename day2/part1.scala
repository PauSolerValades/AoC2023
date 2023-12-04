import scala.io.Source

@main def part1() = {
    
    // load all the file into memory
    val filename: String = "input.txt"
    val games = Source.fromFile(filename).getLines().map(
        _.split(";").map(
            _.split(",").toList //el map aplica linia a linia.
    ).toList

    val processed_games List[List[Int]]
}

//def RBG(game)

def is_possible(game: List[String], green: Int, blue: Int, red: Int) = {
    println(game)
}