import {
  AutocompleteArrayInput,
  FileField,
  FileInput,
  ReferenceArrayInput,
  SelectInput,
  SimpleForm,
  required,
  useGetOne,
} from "react-admin";
import { useLocation } from "react-router-dom";
import { CourierChoices } from "../values/courier-choices";

export const ShipmentForm = () => {
  const { state } = useLocation();
  const selectedIds = state.record?.packingLists;
  const { data: firstSelectedRecord } = useGetOne(
    "packing-list",
    {
      id: selectedIds[0],
    },
    { enabled: selectedIds && selectedIds.length > 0 }
  );

  return (
    <SimpleForm>
      <SelectInput
        source="courier"
        choices={CourierChoices}
        validate={required()}
      />
      <ReferenceArrayInput source="packingLists" reference="packing-list">
        <AutocompleteArrayInput disabled validate={required()} />
      </ReferenceArrayInput>
      {firstSelectedRecord &&
        firstSelectedRecord.shipToCountryCode === "GB" && (
          <FileInput
            source="customsDocuments"
            accept="application/pdf"
            maxSize={5000000}
            validate={required()}
          >
            <FileField source="src" title="title" />
          </FileInput>
        )}
    </SimpleForm>
  );
};
