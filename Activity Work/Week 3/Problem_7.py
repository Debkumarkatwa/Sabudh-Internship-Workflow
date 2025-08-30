def K_Product(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    result = []
    
    for spell in spells:
        left, right = 0, len(potions)

        while left < right:
            mid = (left + right) // 2

            if spell * potions[mid] >= success:
                right = mid
            else:
                left = mid + 1

        result.append(len(potions) - left)
    
    return result


print(K_Product(spells = [5,1,3], potions = [1,2,3,4,5], success = 7 ))
print(K_Product(spells = [3,1,2], potions = [8,5,8], success = 16))