main :: IO ()
main = do
        cases <- readLn
        runCases cases
        where
            runCases n
                | n > 0 = do
                    process
                    runCases (n - 1)
                | otherwise = return ()

process = do
        n <- readLn
        putStrLn $ toWords n

toWords :: Int -> String
toWords 0 = "Zero"
toWords n = let
    groups = reverse $ digitGroups n 4
    make g i = if g == 0 && i /= 3 then join $ ["",""] else join $ [(groupToWords g), (bigs !! (3-i))]
    in
        join $ zipWith make groups [0..]

smalls = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tensWords = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

bigs = ["", "Thousand", "Million", "Billion"]

digitGroups n nGroups = addGroup 4 $ abs n
    where
        addGroup 0 _ = []
        addGroup i x = (x `mod` 1000):(addGroup (i - 1) (x `div` 1000))

groupToWords n = let
    nHundreds = n `div` 100
    hundreds = if nHundreds > 0 then (smalls !! nHundreds) ++ " Hundred" else ""

    left = n `mod` 100
    nTens = left `div` 10
    tens = if nTens >= 2 then join $ [(tensWords !! nTens), (smalls !! (left `mod` 10))] else smalls !! left
    in
        unwords $ if nHundreds > 0 then [hundreds, tens] else [tens]

join :: [String] -> String
join xs = let
    opp s acc = if length s > 0 then s ++ " " ++ acc else acc
    in
        reverse $ dropWhile (== ' ') $ reverse $ foldr opp "" xs
