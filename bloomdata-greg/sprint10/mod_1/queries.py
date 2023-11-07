# How many total Characters are there?
TOTAL_CHARACTERS = "SELECT COUNT(*) FROM charactercreator_character"

TOTAL_DISTINCT_NAMES = "SELECT COUNT(DISTINCT name) FROM charactercreator_character"

# How many of each specific subclass (the necromancer table)?
# TOTAL_NECROMANCER = "..."

# How many total Items?
TOTAL_ITEMS = "SELECT COUNT(*) FROM charactercreator_character_inventory"

TOTAL_DISTINCT_ITEMS = "SELECT COUNT(*) FROM armory_item"
#                    = "SELECT COUNT(DISTINCT item_id) FROM charactercreator_character_inventory"

# How many of the Items are weapons?
WEAPONS = "SELECT COUNT(*) FROM armory_weapon"

# How many of the items are not weapons?
NON_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_item
    LEFT JOIN armory_weapon
    ON armory_item.item_id = armory_weapon.item_ptr_id
    WHERE armory_weapon.power IS NULL
'''

# How many Items does each character have? (Return first 20 rows)
CHARACTER_ITEMS = '''
    SELECT character_id, COUNT(item_id) AS weapons
    FROM charactercreator_character_inventory AS inventory
    GROUP BY inventory.character_id
    LIMIT 20
'''

# How many Weapons does each character have? (Return first 20 rows)
CHARACTER_WEAPONS = '''
    SELECT character_id, COUNT(item_ptr_id) AS items
    FROM charactercreator_character_inventory AS inventory
    LEFT JOIN armory_weapon AS weapon
    ON inventory.item_id = weapon.item_ptr_id
    GROUP BY character_id
    LIMIT 20
'''

# On average, how many Items does each Character have?
AVG_CHARACTER_ITEMS = '''
    SELECT AVG(weapons)
    FROM (SELECT character_id, COUNT(item_id) AS weapons
    FROM charactercreator_character_inventory AS inventory
    GROUP BY inventory.character_id)
'''

# On average, how many Weapons does each character have?
AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(items)
    FROM (SELECT character_id, COUNT(item_ptr_id) AS items
    FROM charactercreator_character_inventory AS inventory
    LEFT JOIN armory_weapon AS weapon
    ON inventory.item_id = weapon.item_ptr_id
    GROUP BY character_id)
'''