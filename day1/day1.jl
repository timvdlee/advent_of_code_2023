# function stringNumParser(line::String)
#     numberDict:: Dict = Dict("one"=>"1","two"=>"2","three"=>"3","four"=>"4","five"=>"5","six"=>"6","seven"=>"7","eight"=>"8","nine"=>"9")
#     for key in keys(numberDict)
#         i = findfirst(key,line)
#         if i !== nothing
#             print(line[i])

#         end
#     end
# end

function stringNumParser(line::String)
    numberDict:: Vector{Pair{String,String}} = ["one"=>"1","two"=>"2","three"=>"3","four"=>"4","five"=>"5","six"=>"6","seven"=>"7","eight"=>"8","nine"=>"9"]
    firstI = nothing
    firstPair = nothing

    for replacer in numberDict
        i = findfirst(replacer[1],line)
        if i !== nothing
            if isnothing(firstI)
                firstI = i
                firstPair = replacer
            else    
                if i < firstI
                    firstI = i
                    firstPair = replacer
                end
            end
        end
    end
    lastI = nothing
    lastPair = nothing
    for replacer in numberDict
        i = findlast(replacer[1],line)
        if i !== nothing
            if isnothing(lastI)
                lastI = i
                lastPair = replacer
            else    
                if i > lastI
                    lastI = i
                    lastPair = replacer
                end
            end
        end
    end

    if !isnothing(firstPair)
        line = replace(line,firstPair)
    end
    if !isnothing(lastPair)
        line = replace(line,lastPair)
    end
    return line
end


function main()
    calNum :: Int64 = 0
    open("day1/input.txt","r") do f
        while ! eof(f)
            lineCalNum :: String = ""
            lineForward:: String = readline(f)
            
            # lineForward = stringNumParser(lineForward) #day2

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
# println(stringNumParser("eightthreewothree"))

