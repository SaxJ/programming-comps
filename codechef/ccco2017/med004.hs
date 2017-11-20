import qualified Data.Map as M

addSeenCount key = M.insertWith (+) key 1

takeSeenCount key = M.insertWith (-) key 1

markSeen :: String -> M.Map Char Int
markSeen = foldr addSeenCount M.empty

removeChef counts = foldr (takeSeenCount counts) "codechef"

isBroken seen = not (any (<= 0) (M.elems seen))

countChefs seen = loop seen 0
    where
        loop marked count = if isBroken next then count else loop next (count + 1)
                                           where
                                               next = removeChef marked

main :: IO ()
main = do
        length <- getLine
        string <- getLine

        let seen = markSeen string
        print seen
        let next = removeChef seen
        --let count = countChefs seen
        print next
        return ()
