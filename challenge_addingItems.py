data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for i in data:
    if "Flower" in i:
        flowers.append(i)

    else:
        shrubs.append(i)
print(flowers)
print(shrubs)
#extended solution below:
flowers = [s.strip('Flower') for s in flowers]
flowers = [s.strip(' - ') for s in flowers]
print(flowers)

shrubs = [s.strip('Shrub') for s in shrubs]
shrubs = [s.strip(' - ') for s in shrubs]
print(shrubs)

shrubs.sort(reverse=True)
print(shrubs)


