


function main()
    calNum :: Int64 = 0
    open("day1/input.txt","r") do f
        while ! eof(f)
            lineCalNum :: String = ""
            lineForward:: String = readline(f)
            lineReverse:: String = reverse(lineForward)
            for charForward in lineForward
                if isnumeric(charForward)
                    lineCalNum *= charForward
                    break
                end
            end
            for charReverse in lineReverse
                if isnumeric(charReverse)
                    lineCalNum *= charReverse
                    break
                end
            end
            calNum += parse(Int,lineCalNum)
        end
    end
    println(calNum)
end


main()