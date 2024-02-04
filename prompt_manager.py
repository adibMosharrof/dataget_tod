class NlgPrompt:
    def get_prompt(
        self,
        domain: str,
        schema: str,
        dialog_history: str,
    ) -> str:
        """
        Returns the NLG prompt for the given domain
        """
        prompt_text = "\n".join(
            [
                f"You are an expert chat assistant for the domain: {domain}.",
                "Instructions: As an expert, you must generate the most appropriate response for the chat assistant.",
                "The response can be an api call or a response to the user.",
                # "If there are search results, you should use information from the search results to generate the response.",
                # "If you think you need more information to answer the user request, you can request information from the user.",
                # "Based on the Last User Utterance, you must find the relevant Intent from the Schema and your request can only use the required slots and optional slots from that Intent.",
                # f"You will be provided with a Schema for domain: {domain}, which contains the relevant Intents for the domain. Each Intent has a list of required and optional slots.",
                f"You will be provided with a Schema for domain: {domain}.",
                schema,
                f"You will be provided an incomplete dialog between a user and a chat assistant, and an optional search results.",
                "Dialog History:",
                dialog_history,
                # "Using the Dialog History, Search Results, relevant Intent from the Schema and by following the Instructions please generate the response for the chat assistant.",
                ". Using the Dialog History, Search Results, and by following the Instructions please generate the response for the chat assistant.",
            ]
        )
        return prompt_text
