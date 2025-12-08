from bootcamp_utils.logger import setup_logger

log = setup_logger()

for i in range(500):
    log.info(f"check the loggin for {i}")
log.info("User log in successful")
log.warning("Unusual behavior detected")
log.error("Database Timed out while fetching User")
log.debug("Debug message — will not show (below INFO level)")
