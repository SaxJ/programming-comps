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
        print $ toWords n

toWords :: Int -> String
toWords n = show n

smalls = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

bigs = ["", "Thousand", "Million", "Billion"]

digitGroups n nGroups = addGroup $ abs n
    where
        addGroup x = (x `mod` 1000):(addGroup (x `div` 1000))
