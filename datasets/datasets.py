BASE_DATASET = {
				'name':'name',
				'id' :'id',
				'iron_pieces':'iron_pcs',
				'tin_pieces':'tin_pcs',
				'copper_pieces':'copper_pcs',
				'bronze_pieces':'bronze_pcs',
				'silver_pieces':'silver_pcs',
				'gold_pieces':'gold_pcs',
				'mithril_pieces':'mithril_pcs',
				'description':'desc'			
}



PLAYER_DATASET={

				'player_name':BASE_DATASET['name'],
				'player_id':BASE_DATASET['id'],
				'player_gold':'gold',
				'player_inventory':'inventory'

				}


ITEM_DATASET = {

						'item_name':BASE_DATASET['name'],
						'item_id':BASE_DATASET['id'],
						'item_price':'price'

					}


PLAYER_DATABASE_DATASET = {

				'filename':'player_database.db',
				'table_name':'player_table'

			 }


ITEM_DATABASE_DATASET = {

						'filename':'item_database.db',
						'table_name':'item_table'

						 }
