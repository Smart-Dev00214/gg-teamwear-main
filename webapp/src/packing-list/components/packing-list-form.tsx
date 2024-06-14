import { DateTimeInput, SelectInput, SimpleForm, TextInput } from "react-admin";
import { PackingListStatusChoices } from "../values/packing-list-status-choices";

export const PackingListForm = () => (
  <SimpleForm>
    <TextInput source="documentNumber" />
    <SelectInput source="status" choices={PackingListStatusChoices} />
    <DateTimeInput source="receivedDate" />
    <TextInput source="shipToGLN" label="Ship to GLN" />
    <TextInput source="shipToName" />
    <TextInput source="shipToAddressLine1" />
    <TextInput source="shipToAddressLine2" />
    <TextInput source="shipToCity" />
    <TextInput source="shipToCountryCode" />
    <TextInput source="shipToPostalCode" />
  </SimpleForm>
);
