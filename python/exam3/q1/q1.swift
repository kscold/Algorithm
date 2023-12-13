import Foundation

func q1(_ A: Int, _ B: Int, _ Skills: [[Int]]) -> Int {
    // your code is here
    // ----------------------------------------------
    // ----------------------------------------------
}

func compareOutput(file1: String, file2: String) {
    do {
        let contents1 = try String(contentsOfFile: file1, encoding: .utf8)
        let contents2 = try String(contentsOfFile: file2, encoding: .utf8)
        
        let lines1 = contents1.components(separatedBy: .newlines)
        let lines2 = contents2.components(separatedBy: .newlines)
        
        var success = true
        
        for (i, (line1, line2)) in zip(lines1, lines2).enumerated() {
            if line1 != line2 {
                print("[\(i + 1)] Wrong answer: Yours='\(line1)', Expected='\(line2)'")
                success = false
                break
            }
        }
        
        if success {
            print("Success!")
        }
    } catch {
        print("Error reading files: \(error)")
    }
}

func main() {
    let inputFilePath = "input.txt"
    let outputFilePath = "output.txt"

    do {
        let inputData = try String(contentsOfFile: inputFilePath)
        var outputData = ""
        let start_time = CFAbsoluteTimeGetCurrent()


        let lines = inputData.components(separatedBy: .newlines)
        guard let K = Int(lines[0]) else { return }

        var currentIndex = 1
        for _ in 0..<K {
            let tokens = lines[currentIndex].split(separator: " ").compactMap { Int($0) }
            guard tokens.count >= 2 else { continue }
            let S = tokens[0]
            let N = tokens[1]
            currentIndex += 1

            var skills = Array(repeating: Array(repeating: 0, count: S), count: N)
            for j in 0..<N {
                let skillLine = lines[currentIndex + j].split(separator: " ").compactMap { Int($0) }
                skills[j] = skillLine
            }
            currentIndex += N

            let result = q1(S, N, skills) // Implement the solution function according to your logic
            print(result)
            outputData += "\(result)\n"
        }

        try outputData.write(to: URL(fileURLWithPath: outputFilePath), atomically: true, encoding: .utf8)
        
        if let expectedURL = Bundle.main.url(forResource: "expected", withExtension: "txt"),
           let outputURL = Bundle.main.url(forResource: "output", withExtension: "txt") {
            compareOutput(file1: outputURL.path, file2: expectedURL.path)
        }
        
        let end_time = CFAbsoluteTimeGetCurrent()
        print("Elapsed time: \(end_time - start_time) seconds.")
    }
    catch {   
        print("Error")
    }
}

main()
