import Data.Time.Calendar
import Control.Monad
import Data.Time.Calendar.WeekDate

main :: IO ()
main = do
    cases <- readLn
    replicateM_ cases testCase

testCase :: IO ()
testCase = do
    fromLine <- getLine
    let from = [read x | x <- words fromLine]
    toLine <- getLine
    let to = [read x | x <- words toLine]
    putStrLn $ show $ calculate from to

calculate :: [Int] -> [Int] -> Int
calculate [fy, fm, fd] [ty, tm, td] =
    let
        fromMonth = if fd > 1 then fm + 1 else fm
        fromYear = toInteger $ if fromMonth > 12 then fy + 1 else fy
        fromDay = fromGregorian fromYear (if fromMonth > 12 then 1 else fromMonth) 1
        toDay = fromGregorian (toInteger ty) tm td
    in
        sundaysInRange fromDay toDay

addMonth :: Day -> Day
addMonth day =
    let
        (y, m, d) = toGregorian day
        mm = if m + 1 > 12 then 1 else m + 1
        yy = if mm == 1 then y + 1 else y
    in
        fromGregorian yy mm d

third (_, _, a) = a

sundaysInRange :: Day -> Day -> Int
sundaysInRange fromDay toDay =
    sundays fromDay toDay 0
    where
        sundays from to count
            | from > to = count
            | (third $ (toWeekDate from)) == 7 = sundays (addMonth from) to (count + 1)
            | otherwise = sundays (addMonth from) to count
