import Foundation

func q2(_ n: Int, _ coords: [[Int]]) -> Int {
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
    // DO NOT EDIT main() function
    
    var R = 0
    var N = 0
    var result = 0
    
    let start_time = CFAbsoluteTimeGetCurrent()

    FileManager.default.createFile(atPath: "output.txt", contents: nil, attributes: nil)
 
    var str = ""
    
    if let inputURL = Bundle.main.url(forResource: "input", withExtension: "txt"),
       let input = try? String(contentsOf: inputURL, encoding: .utf8),
       let outputURL = Bundle.main.url(forResource: "output", withExtension: "txt") {
        
        let inputLines = input.components(separatedBy: .newlines)
        
        if let r = Int(inputLines[0]) {
            R = r
        }
        if let n = Int(inputLines[1]) {
            N = n
        }

        var coords = Array(repeating: Array(repeating: 0, count: 2), count: N)
        
        for i in 1..<(N + 1) {
            let line = inputLines[i]
            let components = line.components(separatedBy: " ")
            
            if components.count == 2,
                let x = Int(components[0]),
                let y = Int(components[1]) {
                coords[i][0] = x
                coords[i][1] = y
            }
        }
        result = q2(R, coords)
        print(result)
        if str == "" {
            str = String(result)
        }
        else {
            str = str + "\n" + String(result)
        }
        do {
            try str.write(to: outputURL, atomically: true, encoding: .utf8)
        } catch {
            print("File write error")
        }
        
        if let expectedURL = Bundle.main.url(forResource: "expected", withExtension: "txt") {
            compareOutput(file1: outputURL.path, file2: expectedURL.path)
        }
        
        let end_time = CFAbsoluteTimeGetCurrent()
        print("Elapsed time: \(end_time - start_time) seconds.")
    }
    else {
        print("error?")
    }
}

main()
