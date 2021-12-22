def organiza_por_media(nums):
    media = 0
    contador = 0
    for i in range(len(nums)):
        media += nums[i] 
        contador += 1
    if media > 0 and contador > 0:
        conta = media / contador
    for numero in nums:
        for i in range(len(nums) - 1):
            if nums[i] > conta:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

