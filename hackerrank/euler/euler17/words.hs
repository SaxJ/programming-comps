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
        print $ digitGroups n 4
        print $ [groupToWords x | x <- digitGroups n 4]
        putStrLn $ toWords n

toWords :: Int -> String
toWords n = let
    g = digitGroups n 4
    groups = [groupToWords x | x <- g]
    build (a, b) ac = let
        pre = b ++ " " ++ (bigs !! a)
        in
            if (g !! a) /= 0 then pre ++ ac else ac
    in
        foldr build ""  $ zip [0..] groups

smalls = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tensWords = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

bigs = ["", "Thousand", "Million", "Billion"]

digitGroups n nGroups = addGroup 4 $ abs n
    where
        addGroup 0 _ = []
        addGroup i x = (x `mod` 1000):(addGroup (i - 1) (x `div` 1000))

groupToWords n = let
    hundreds = n `div` 100
    nTens = n `mod` 100

    tens = nTens  `div` 10
    units = nTens `mod` 10

    hundredText = if hundreds /= 0 then "" else (smalls !! hundreds) ++ " Hundred"
    in
        if tens >= 2 then hundredText ++ (tensWords !! tens) ++ (if units /= 0 then smalls !! units else "") else (if nTens /= 0 then hundredText ++ (smalls !! nTens) else "")
